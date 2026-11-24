"""Invented NTFS-like name observations; no live filesystem access."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Name:
    parent_index: int
    parent_sequence: int
    text: str

@dataclass(frozen=True)
class Snapshot:
    volume: str
    index: int
    sequence: int
    names: tuple[Name, ...]

def classify(before, after, old, new):
    if (before.volume,before.index,before.sequence) != (
        after.volume,after.index,after.sequence):
        return "FILE_IDENTITY_CONFLICT"
    if old not in before.names or new not in after.names:
        return "MISSING_NAME_EVIDENCE"
    if old == new:
        return "UNCHANGED_NAME_REFERENCE"
    if old in after.names:
        return "OLD_REFERENCE_REMAINS"
    if len(before.names)>1 or len(after.names)>1:
        return "MULTIPLE_LINK_CONTEXT"
    if old.parent_index == new.parent_index:
        if old.parent_sequence != new.parent_sequence:
            return "PARENT_IDENTITY_UNCERTAIN"
        return "SAME_PARENT_RENAME_CANDIDATE"
    return "CROSS_PARENT_MOVE_CANDIDATE"

def main():
    old = Name(10,1,"report.txt")
    renamed = Name(10,1,"summary.txt")
    moved = Name(20,1,"report.txt")
    reused = Name(10,2,"summary.txt")
    before = Snapshot("V",42,7,(old,))
    def after(*names):
        return Snapshot("V",42,7,names)
    cases = [
        (after(renamed),renamed,"SAME_PARENT_RENAME_CANDIDATE"),
        (after(moved),moved,"CROSS_PARENT_MOVE_CANDIDATE"),
        (after(reused),reused,"PARENT_IDENTITY_UNCERTAIN"),
        (after(old,renamed),renamed,"OLD_REFERENCE_REMAINS"),
        (after(renamed,Name(30,1,"link.txt")),renamed,"MULTIPLE_LINK_CONTEXT"),
        (after(old),renamed,"MISSING_NAME_EVIDENCE"),
        (after(old),old,"UNCHANGED_NAME_REFERENCE"),
        (Snapshot("V",42,8,(renamed,)),renamed,"FILE_IDENTITY_CONFLICT"),
        (Snapshot("OTHER",42,7,(renamed,)),renamed,"FILE_IDENTITY_CONFLICT"),
    ]
    for snapshot,target,expected in cases:
        result = classify(before,snapshot,old,target)
        assert result == expected,(result,expected)
        print(result)
    print(f"{len(cases)}/{len(cases)} synthetic parent-reference checks passed")

if __name__ == "__main__":
    main()
