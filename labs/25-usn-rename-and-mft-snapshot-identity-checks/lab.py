"""Fictional USN rename pair and MFT snapshot consistency; no NTFS access."""
from dataclasses import dataclass

# Fictional reason bits only: NOT actual Win32 USN reason constants.
OLD_NAME = 1
NEW_NAME = 2

@dataclass(frozen=True)
class UsnEvent:
    volume: str
    file_index: int
    sequence: int
    usn: int
    time: int
    reason: int
    name: str

@dataclass(frozen=True)
class MftSnapshot:
    volume: str
    file_index: int
    sequence: int
    name: str
    collected_at: int

def triage(old: UsnEvent | None, new: UsnEvent,
           before: MftSnapshot | None, after: MftSnapshot | None,
           collection_gap: bool = False) -> str:
    if old is None or not (old.reason & OLD_NAME) or not (new.reason & NEW_NAME):
        return "INSUFFICIENT_USN"
    if old.usn >= new.usn or old.time > new.time:
        return "ORDER_CONFLICT"
    identity = (new.volume, new.file_index, new.sequence)
    if (old.volume, old.file_index, old.sequence) != identity:
        return "USN_IDENTITY_CONFLICT"
    if collection_gap:
        return "UNCERTAIN_COLLECTION"
    if before is None or after is None:
        return "PARTIAL_SNAPSHOTS"
    for snapshot in (before, after):
        if (snapshot.volume, snapshot.file_index) != identity[:2]:
            return "UNRELATED_SNAPSHOT"
        if snapshot.sequence != new.sequence:
            return "FILE_REFERENCE_REUSE"
    if before.collected_at > new.time or after.collected_at < new.time:
        return "SNAPSHOT_TIMING_CONFLICT"
    if before.name != old.name or after.name != new.name:
        return "SNAPSHOT_NAME_CONFLICT"
    return "CONSISTENT_CANDIDATE"

def main():
    old = UsnEvent("V1", 42, 7, 100, 100, OLD_NAME, "before.txt")
    new = UsnEvent("V1", 42, 7, 104, 105, NEW_NAME, "after.txt")
    before = MftSnapshot("V1", 42, 7, "before.txt", 99)
    after = MftSnapshot("V1", 42, 7, "after.txt", 106)
    cases = [
        ("consistent candidate", old, new, before, after, False, "CONSISTENT_CANDIDATE"),
        ("missing before snapshot", old, new, None, after, False, "PARTIAL_SNAPSHOTS"),
        ("known collection gap", old, new, before, after, True, "UNCERTAIN_COLLECTION"),
        ("USN file reference differs", old, UsnEvent("V1",42,8,104,105,NEW_NAME,"after.txt"), before, after, False, "USN_IDENTITY_CONFLICT"),
        ("MFT sequence changed", old, new, before, MftSnapshot("V1",42,8,"after.txt",106), False, "FILE_REFERENCE_REUSE"),
        ("MFT name conflicts", old, new, before, MftSnapshot("V1",42,7,"other.txt",106), False, "SNAPSHOT_NAME_CONFLICT"),
        ("unrelated volume", old, new, MftSnapshot("V2",42,7,"before.txt",99), after, False, "UNRELATED_SNAPSHOT"),
        ("wrong time order", old, new, before, MftSnapshot("V1",42,7,"after.txt",102), False, "SNAPSHOT_TIMING_CONFLICT"),
        ("missing old USN", None, new, before, after, False, "INSUFFICIENT_USN"),
        ("USN sequence reversed", UsnEvent("V1",42,7,108,100,OLD_NAME,"before.txt"), new, before, after, False, "ORDER_CONFLICT"),
    ]
    for label, o, n, b, a, gap, expected in cases:
        result = triage(o, n, b, a, gap)
        assert result == expected, (label, result)
        print(f"{label:32} {result}")
    print(f"{len(cases)}/{len(cases)} fictional NTFS consistency checks passed")

if __name__ == "__main__":
    main()
