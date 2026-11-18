"""Synthetic USN rename reason flags and ambiguous candidates; no NTFS access."""
from dataclasses import dataclass

# Invented bit positions for the teaching model, NOT Win32 flag constants.
OLD_NAME = 1 << 0
NEW_NAME = 1 << 1
CLOSE = 1 << 2
DATA_CHANGE = 1 << 3

@dataclass(frozen=True)
class Event:
    volume: str
    file_id: int
    toy_epoch: int
    usn: int
    reason: int
    name: str

def candidates(new_event: Event, previous: list[Event], gap: int = 3) -> list[Event]:
    if not (new_event.reason & NEW_NAME):
        return []
    result = []
    for old in previous:
        same_identity = (old.volume, old.file_id, old.toy_epoch) == (
            new_event.volume, new_event.file_id, new_event.toy_epoch
        )
        if (same_identity and (old.reason & OLD_NAME)
                and 0 < new_event.usn - old.usn <= gap):
            result.append(old)
    return sorted(result, key=lambda x: x.usn)

def label(new_event: Event, previous: list[Event]) -> str:
    options = candidates(new_event, previous)
    if len(options) > 1:
        return "AMBIGUOUS"
    return "PAIR_CANDIDATE" if options else "INSUFFICIENT"

def main():
    base = Event("V1", 42, 1, 100, OLD_NAME | CLOSE, "original.txt")
    new = Event("V1", 42, 1, 101, NEW_NAME | CLOSE, "renamed.txt")
    checks = [
        ("combined reason flags", label(new, [base]), "PAIR_CANDIDATE"),
        ("two candidate old names", label(new, [
            base, Event("V1", 42, 1, 99, OLD_NAME, "earlier.txt")]), "AMBIGUOUS"),
        ("missing old record", label(new, []), "INSUFFICIENT"),
        ("different file id", label(new, [
            Event("V1", 43, 1, 100, OLD_NAME, "a")]), "INSUFFICIENT"),
        ("different volume", label(new, [
            Event("V2", 42, 1, 100, OLD_NAME, "a")]), "INSUFFICIENT"),
        ("different toy epoch", label(new, [
            Event("V1", 42, 2, 100, OLD_NAME, "a")]), "INSUFFICIENT"),
        ("wrong order", label(new, [
            Event("V1", 42, 1, 102, OLD_NAME, "a")]), "INSUFFICIENT"),
        ("too far apart", label(new, [
            Event("V1", 42, 1, 90, OLD_NAME, "a")]), "INSUFFICIENT"),
        ("no old bit", label(new, [
            Event("V1", 42, 1, 100, DATA_CHANGE, "a")]), "INSUFFICIENT"),
        ("no new bit", label(Event("V1", 42, 1, 101, DATA_CHANGE, "a"),
                             [base]), "INSUFFICIENT"),
    ]
    for title, actual, expected in checks:
        assert actual == expected, (title, actual)
        print(f"{title:26} {actual}")
    print("10/10 synthetic USN flag and ambiguity checks passed")

if __name__ == "__main__":
    main()
