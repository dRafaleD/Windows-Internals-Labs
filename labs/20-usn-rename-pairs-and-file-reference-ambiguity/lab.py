"""Offline toy NTFS USN rename-pair correlation; not a real journal parser."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Record:
    volume: str
    file_id: int
    toy_epoch: int
    usn: int
    reason: str
    name: str

OLD = "RENAME_OLD_NAME"
NEW = "RENAME_NEW_NAME"

def pair(old: Record, new: Record) -> bool:
    return (
        old.reason == OLD and new.reason == NEW
        and (old.volume, old.file_id, old.toy_epoch)
            == (new.volume, new.file_id, new.toy_epoch)
        and old.usn < new.usn
        and 0 < new.usn - old.usn <= 3
    )

def main() -> None:
    before = Record("VOL1", 42, 1, 100, OLD, "old.txt")
    after = Record("VOL1", 42, 1, 101, NEW, "new.txt")
    cases = [
        ("same toy object and adjacent records", before, after, True),
        ("different file ID", before, Record("VOL1", 43, 1, 101, NEW, "new.txt"), False),
        ("different volume", before, Record("VOL2", 42, 1, 101, NEW, "new.txt"), False),
        ("reused numeric ID, different epoch", before, Record("VOL1", 42, 2, 101, NEW, "new.txt"), False),
        ("reversed journal ordering", before, Record("VOL1", 42, 1, 99, NEW, "new.txt"), False),
        ("same journal number", before, Record("VOL1", 42, 1, 100, NEW, "new.txt"), False),
        ("large record gap", before, Record("VOL1", 42, 1, 120, NEW, "new.txt"), False),
        ("wrong reason type", before, Record("VOL1", 42, 1, 101, "FILE_CREATE", "new.txt"), False),
        ("wrong initial reason", Record("VOL1", 42, 1, 100, "FILE_DELETE", "old.txt"), after, False),
    ]
    for label, old, new, expected in cases:
        actual = pair(old, new)
        assert actual is expected, (label, actual)
        print(f"{label:39} {'PAIR_CANDIDATE' if actual else 'NO_PAIR'}")
    print("9/9 synthetic USN-pair checks passed")
    print("Pair candidates are not proof of a complete NTFS rename history.")

if __name__ == "__main__":
    main()
