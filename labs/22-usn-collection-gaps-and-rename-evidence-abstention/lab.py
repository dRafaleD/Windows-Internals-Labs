"""Synthetic USN rename triage with explicit collection-gap metadata; no NTFS I/O."""
from dataclasses import dataclass

# Invented flags; not real Windows API constants.
OLD = 1
NEW = 2
CLOSE = 4

@dataclass(frozen=True)
class Record:
    volume: str
    file_id: int
    toy_epoch: int
    usn: int
    reason: int
    name: str

def gap_between(left: int, right: int,
                unavailable_ranges: list[tuple[int, int]]) -> bool:
    # Ranges represent known missing COLLECTION COVERAGE, not numeric USN gaps.
    for start, end in unavailable_ranges:
        if start <= end and start < right and end > left:
            return True
    return False

def classify(new: Record, older: list[Record],
             unavailable_ranges: list[tuple[int, int]]) -> str:
    if not new.reason & NEW:
        return "INSUFFICIENT"
    matches = [
        old for old in older
        if old.reason & OLD
        and (old.volume, old.file_id, old.toy_epoch)
            == (new.volume, new.file_id, new.toy_epoch)
        and old.usn < new.usn
    ]
    if len(matches) > 1:
        return "AMBIGUOUS"
    if not matches:
        return "INSUFFICIENT"
    if gap_between(matches[0].usn, new.usn, unavailable_ranges):
        return "UNCERTAIN_GAP"
    return "PAIR_CANDIDATE"

def main():
    previous = Record("V1", 42, 1, 100, OLD | CLOSE, "old.txt")
    current = Record("V1", 42, 1, 104, NEW | CLOSE, "new.txt")
    cases = [
        ("single candidate", current, [previous], [], "PAIR_CANDIDATE"),
        ("known collection gap", current, [previous], [(101, 103)], "UNCERTAIN_GAP"),
        ("gap outside interval", current, [previous], [(110, 120)], "PAIR_CANDIDATE"),
        ("two plausible names", current, [previous, Record("V1", 42, 1, 102, OLD, "other.txt")], [], "AMBIGUOUS"),
        ("different file ID", current, [Record("V1", 43, 1, 100, OLD, "old.txt")], [], "INSUFFICIENT"),
        ("different volume", current, [Record("V2", 42, 1, 100, OLD, "old.txt")], [], "INSUFFICIENT"),
        ("different toy epoch", current, [Record("V1", 42, 2, 100, OLD, "old.txt")], [], "INSUFFICIENT"),
        ("wrong old flag", current, [Record("V1", 42, 1, 100, CLOSE, "old.txt")], [], "INSUFFICIENT"),
        ("missing new flag", Record("V1", 42, 1, 104, CLOSE, "new.txt"), [previous], [], "INSUFFICIENT"),
        ("reverse order", current, [Record("V1", 42, 1, 106, OLD, "late.txt")], [], "INSUFFICIENT"),
        ("same USN", current, [Record("V1", 42, 1, 104, OLD, "old.txt")], [], "INSUFFICIENT"),
    ]
    for name, new, history, gaps, expected in cases:
        actual = classify(new, history, gaps)
        assert actual == expected, (name, actual)
        print(f"{name:27} {actual}")
    print(f"{len(cases)}/{len(cases)} synthetic rename-evidence checks passed")

if __name__ == "__main__":
    main()
