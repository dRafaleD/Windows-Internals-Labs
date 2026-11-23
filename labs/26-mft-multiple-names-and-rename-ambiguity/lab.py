"""Synthetic USN and MFT snapshots: multiple names complicate rename conclusions."""
from dataclasses import dataclass

# Invented flags, NOT actual NTFS USN_REASON constants.
RENAME_OLD = 1
RENAME_NEW = 2

@dataclass(frozen=True)
class Usn:
    volume: str
    file_index: int
    reference_sequence: int
    usn: int
    time: int
    reason: int
    name: str

@dataclass(frozen=True)
class Snapshot:
    volume: str
    file_index: int
    reference_sequence: int
    time: int
    names: tuple[str, ...]

def classify(old: Usn | None, new: Usn,
             before: Snapshot | None, after: Snapshot | None,
             collection_gap: bool = False) -> str:
    if old is None or not (old.reason & RENAME_OLD) or not (new.reason & RENAME_NEW):
        return "INSUFFICIENT_USN"
    if old.usn >= new.usn or old.time > new.time:
        return "ORDER_CONFLICT"
    identity = (new.volume, new.file_index, new.reference_sequence)
    if (old.volume, old.file_index, old.reference_sequence) != identity:
        return "USN_IDENTITY_CONFLICT"
    if collection_gap:
        return "UNCERTAIN_COLLECTION"
    if before is None or after is None:
        return "PARTIAL_SNAPSHOTS"
    for snap in (before, after):
        if (snap.volume, snap.file_index) != identity[:2]:
            return "UNRELATED_SNAPSHOT"
        if snap.reference_sequence != identity[2]:
            return "FILE_REFERENCE_REUSE"
    if before.time > old.time or after.time < new.time:
        return "SNAPSHOT_TIMING_CONFLICT"
    if old.name not in before.names or new.name not in after.names:
        return "SNAPSHOT_NAME_CONFLICT"
    if old.name in after.names:
        return "OLD_NAME_STILL_PRESENT"
    if len(after.names) > 1 or len(before.names) > 1:
        return "MULTI_NAME_CONTEXT"
    return "CONSISTENT_CANDIDATE"

def main():
    old = Usn("VOL", 42, 7, 100, 100, RENAME_OLD, "old.txt")
    new = Usn("VOL", 42, 7, 104, 105, RENAME_NEW, "new.txt")
    before = Snapshot("VOL", 42, 7, 99, ("old.txt",))
    after = Snapshot("VOL", 42, 7, 106, ("new.txt",))
    cases = [
        ("one-name candidate", old,new,before,after,False,"CONSISTENT_CANDIDATE"),
        ("old name also remains", old,new,before,Snapshot("VOL",42,7,106,("old.txt","new.txt")),False,"OLD_NAME_STILL_PRESENT"),
        ("extra surviving name", old,new,before,Snapshot("VOL",42,7,106,("new.txt","link.txt")),False,"MULTI_NAME_CONTEXT"),
        ("multiple earlier names", old,new,Snapshot("VOL",42,7,99,("old.txt","shared.txt")),after,False,"MULTI_NAME_CONTEXT"),
        ("missing new name", old,new,before,Snapshot("VOL",42,7,106,("other.txt",)),False,"SNAPSHOT_NAME_CONFLICT"),
        ("known collection gap", old,new,before,after,True,"UNCERTAIN_COLLECTION"),
        ("missing MFT snapshot", old,new,before,None,False,"PARTIAL_SNAPSHOTS"),
        ("reference sequence reuse", old,new,before,Snapshot("VOL",42,8,106,("new.txt",)),False,"FILE_REFERENCE_REUSE"),
        ("wrong volume snapshot", old,new,Snapshot("OTHER",42,7,99,("old.txt",)),after,False,"UNRELATED_SNAPSHOT"),
        ("snapshot recorded too early", old,new,before,Snapshot("VOL",42,7,103,("new.txt",)),False,"SNAPSHOT_TIMING_CONFLICT"),
        ("USN identity differs", old,Usn("VOL",42,8,104,105,RENAME_NEW,"new.txt"),before,after,False,"USN_IDENTITY_CONFLICT"),
        ("no old reason", Usn("VOL",42,7,100,100,0,"old.txt"),new,before,after,False,"INSUFFICIENT_USN"),
    ]
    for label,o,n,b,a,gap,expected in cases:
        got=classify(o,n,b,a,gap)
        assert got==expected,(label,got)
        print(f"{label:31} {got}")
    print(f"{len(cases)}/{len(cases)} synthetic multi-name checks passed")

if __name__ == "__main__":
    main()
