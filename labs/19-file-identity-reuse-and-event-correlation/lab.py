"""Offline file-identity correlation with numeric ID reuse and path changes."""
from dataclasses import dataclass

@dataclass(frozen=True)
class Evidence:
    volume: str
    file_id: int
    epoch: int  # Fictional training marker, not a guaranteed NTFS field.
    path: str
    content_hash: str
    observed_at: int

ORIGIN = Evidence("VOL-A", 42, 1, "C:/Lab/old.txt", "sha-A", 10)

def compare(a: Evidence, b: Evidence) -> str:
    if a.volume == b.volume and a.file_id == b.file_id:
        if a.epoch == b.epoch:
            return "SAME_TOY_OBJECT"
        return "REUSED_NUMERIC_ID"
    if a.path == b.path:
        return "PATH_REUSED"
    if a.content_hash == b.content_hash:
        return "SAME_CONTENT_ONLY"
    return "NO_DIRECT_LINK"

def time_order(a: Evidence, b: Evidence) -> str:
    return "EARLIER" if a.observed_at < b.observed_at else (
        "SAME_TIME" if a.observed_at == b.observed_at else "LATER"
    )

def main():
    cases = [
        ("unchanged", ORIGIN, "SAME_TOY_OBJECT", "SAME_TIME"),
        ("renamed", Evidence("VOL-A", 42, 1, "C:/Lab/new.txt", "sha-A", 12),
         "SAME_TOY_OBJECT", "EARLIER"),
        ("id recycled", Evidence("VOL-A", 42, 2, "C:/Lab/new.txt", "sha-B", 40),
         "REUSED_NUMERIC_ID", "EARLIER"),
        ("old name reused", Evidence("VOL-A", 77, 1, "C:/Lab/old.txt", "sha-B", 50),
         "PATH_REUSED", "EARLIER"),
        ("identical copy", Evidence("VOL-A", 80, 1, "C:/Lab/copy.txt", "sha-A", 20),
         "SAME_CONTENT_ONLY", "EARLIER"),
        ("other volume", Evidence("VOL-B", 42, 1, "D:/Lab/copy.txt", "sha-A", 30),
         "SAME_CONTENT_ONLY", "EARLIER"),
        ("unrelated", Evidence("VOL-A", 99, 1, "C:/Lab/other.txt", "sha-B", 20),
         "NO_DIRECT_LINK", "EARLIER"),
        ("earlier observation", Evidence("VOL-A", 42, 1, "C:/Lab/new.txt", "sha-A", 5),
         "SAME_TOY_OBJECT", "LATER"),
    ]
    for name, record, expected_relation, expected_order in cases:
        relation, order = compare(ORIGIN, record), time_order(ORIGIN, record)
        assert (relation, order) == (expected_relation, expected_order), name
        print(f"{name:21} relation={relation:19} order={order}")
    print("8/8 synthetic identity-correlation cases passed")
    print("Epoch is artificial; no actual Windows file ID or USN record read.")

if __name__ == "__main__":
    main()
