"""Toy USN rename correlation with independent process-context observations."""
from dataclasses import dataclass

# Invented reason flags; these are NOT Windows constants.
OLD_NAME = 1
NEW_NAME = 2

@dataclass(frozen=True)
class Usn:
    volume: str
    file_id: int
    toy_epoch: int
    usn: int
    reason: int
    time: int

@dataclass(frozen=True)
class ProcessEvent:
    volume: str
    file_id: int
    toy_epoch: int
    time: int
    process_guid: str
    kind: str

def has_collection_gap(first: int, last: int, gaps: list[tuple[int,int]]) -> bool:
    return any(start <= end and start < last and end > first
               for start,end in gaps)

def triage(new: Usn, old_records: list[Usn],
           gaps: list[tuple[int,int]],
           process_events: list[ProcessEvent]) -> str:
    if not (new.reason & NEW_NAME):
        return "INSUFFICIENT"
    candidates = [
        old for old in old_records
        if old.reason & OLD_NAME and old.usn < new.usn
        and (old.volume, old.file_id, old.toy_epoch) ==
            (new.volume, new.file_id, new.toy_epoch)
    ]
    if len(candidates) > 1:
        return "AMBIGUOUS_OLD_NAME"
    if not candidates:
        return "INSUFFICIENT"
    if has_collection_gap(candidates[0].usn, new.usn, gaps):
        return "UNCERTAIN_COLLECTION"
    contexts = {
        p.process_guid for p in process_events
        if p.kind == "RENAME" and p.process_guid
        and (p.volume,p.file_id,p.toy_epoch) == (new.volume,new.file_id,new.toy_epoch)
        and abs(p.time-new.time) <= 2
    }
    if len(contexts) > 1:
        return "AMBIGUOUS_PROCESS_CONTEXT"
    return "PAIR_WITH_CONTEXT" if contexts else "PAIR_ONLY"

def main():
    old = Usn("VOL-1",42,1,100,OLD_NAME,200)
    new = Usn("VOL-1",42,1,104,NEW_NAME,205)
    p = ProcessEvent("VOL-1",42,1,205,"process-a","RENAME")
    checks = [
        ("USN pair with process context", triage(new,[old],[],[p]), "PAIR_WITH_CONTEXT"),
        ("USN pair only", triage(new,[old],[],[]), "PAIR_ONLY"),
        ("collection gap", triage(new,[old],[(101,103)],[p]), "UNCERTAIN_COLLECTION"),
        ("two old-name candidates", triage(new,[old,Usn("VOL-1",42,1,102,OLD_NAME,202)],[],[p]), "AMBIGUOUS_OLD_NAME"),
        ("other file context", triage(new,[old],[],[ProcessEvent("VOL-1",43,1,205,"other","RENAME")]), "PAIR_ONLY"),
        ("wrong epoch context", triage(new,[old],[],[ProcessEvent("VOL-1",42,2,205,"other","RENAME")]), "PAIR_ONLY"),
        ("late process event", triage(new,[old],[],[ProcessEvent("VOL-1",42,1,215,"later","RENAME")]), "PAIR_ONLY"),
        ("two process contexts", triage(new,[old],[],[p,ProcessEvent("VOL-1",42,1,204,"process-b","RENAME")]), "AMBIGUOUS_PROCESS_CONTEXT"),
        ("missing old-name record", triage(new,[],[],[p]), "INSUFFICIENT"),
        ("wrong reason", triage(Usn("VOL-1",42,1,104,0,205),[old],[],[p]), "INSUFFICIENT"),
    ]
    for label, actual, expected in checks:
        assert actual == expected, (label,actual)
        print(f"{label:29} {actual}")
    print(f"{len(checks)}/{len(checks)} synthetic USN/process checks passed")

if __name__ == "__main__":
    main()
