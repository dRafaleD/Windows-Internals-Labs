"""Toy USN/process correlation using uncertain timestamp intervals."""
from dataclasses import dataclass

# Made-up flags, not Win32/NTFS constants.
OLD_NAME = 1
NEW_NAME = 2

@dataclass(frozen=True)
class Usn:
    volume: str
    file_id: int
    toy_epoch: int
    usn: int
    reason: int
    second: int
    uncertainty: int

@dataclass(frozen=True)
class ProcessEvidence:
    volume: str
    file_id: int
    toy_epoch: int
    guid: str
    second: int
    uncertainty: int
    kind: str

def possible_time_match(a_second: int, a_uncertainty: int,
                        b_second: int, b_uncertainty: int,
                        tolerance: int = 2) -> bool:
    return max(0, abs(a_second - b_second) -
               a_uncertainty - b_uncertainty) <= tolerance

def known_gap(old_usn: int, new_usn: int,
              unavailable_ranges: list[tuple[int, int]]) -> bool:
    return any(start <= end and start < new_usn and end > old_usn
               for start, end in unavailable_ranges)

def triage(new: Usn, prior: list[Usn],
           process_events: list[ProcessEvidence],
           missing_ranges: list[tuple[int, int]]) -> str:
    if new.uncertainty < 0 or any(x.uncertainty < 0 for x in prior):
        return "INVALID_UNCERTAINTY"
    if any(x.uncertainty < 0 for x in process_events):
        return "INVALID_UNCERTAINTY"
    if not (new.reason & NEW_NAME):
        return "INSUFFICIENT"
    old_candidates = [
        x for x in prior if x.reason & OLD_NAME and x.usn < new.usn
        and (x.volume, x.file_id, x.toy_epoch) ==
            (new.volume, new.file_id, new.toy_epoch)
    ]
    if len(old_candidates) > 1:
        return "AMBIGUOUS_OLD_NAME"
    if not old_candidates:
        return "INSUFFICIENT"
    if known_gap(old_candidates[0].usn, new.usn, missing_ranges):
        return "UNCERTAIN_COLLECTION"
    guids = {
        p.guid for p in process_events
        if p.kind == "RENAME" and p.guid
        and (p.volume, p.file_id, p.toy_epoch) ==
            (new.volume, new.file_id, new.toy_epoch)
        and possible_time_match(new.second, new.uncertainty,
                                p.second, p.uncertainty)
    }
    if len(guids) > 1:
        return "AMBIGUOUS_CONTEXT"
    return "PAIR_WITH_POSSIBLE_CONTEXT" if guids else "PAIR_ONLY"

def main() -> None:
    old = Usn("V1", 42, 1, 100, OLD_NAME, 200, 1)
    new = Usn("V1", 42, 1, 104, NEW_NAME, 205, 1)
    p = ProcessEvidence("V1", 42, 1, "p-a", 206, 1, "RENAME")
    cases = [
        ("matching interval", triage(new, [old], [p], []), "PAIR_WITH_POSSIBLE_CONTEXT"),
        ("far outside interval", triage(new, [old], [ProcessEvidence("V1",42,1,"p-a",230,0,"RENAME")], []), "PAIR_ONLY"),
        ("uncertainty widens overlap", triage(new, [old], [ProcessEvidence("V1",42,1,"p-a",210,4,"RENAME")], []), "PAIR_WITH_POSSIBLE_CONTEXT"),
        ("two possible processes", triage(new, [old], [p,ProcessEvidence("V1",42,1,"p-b",204,0,"RENAME")], []), "AMBIGUOUS_CONTEXT"),
        ("known acquisition gap", triage(new, [old], [p], [(101, 103)]), "UNCERTAIN_COLLECTION"),
        ("no old record", triage(new, [], [p], []), "INSUFFICIENT"),
        ("ambiguous old names", triage(new, [old, Usn("V1",42,1,102,OLD_NAME,202,1)], [p], []), "AMBIGUOUS_OLD_NAME"),
        ("wrong file process", triage(new, [old], [ProcessEvidence("V1",43,1,"other",206,1,"RENAME")], []), "PAIR_ONLY"),
        ("wrong toy epoch", triage(new, [old], [ProcessEvidence("V1",42,2,"other",206,1,"RENAME")], []), "PAIR_ONLY"),
        ("bad new uncertainty", triage(Usn("V1",42,1,104,NEW_NAME,205,-1), [old], [p], []), "INVALID_UNCERTAINTY"),
        ("bad process uncertainty", triage(new, [old], [ProcessEvidence("V1",42,1,"p-a",206,-1,"RENAME")], []), "INVALID_UNCERTAINTY"),
        ("no rename bit", triage(Usn("V1",42,1,104,0,205,1), [old], [p], []), "INSUFFICIENT"),
    ]
    for title, actual, expected in cases:
        assert actual == expected, (title, actual)
        print(f"{title:33} {actual}")
    print(f"{len(cases)}/{len(cases)} synthetic timestamp-correlation cases passed")

if __name__ == "__main__":
    main()
