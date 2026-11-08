"""Toy Windows file-sharing compatibility, with synthetic handles only."""
from dataclasses import dataclass

READ = 0b001
WRITE = 0b010
DELETE = 0b100

@dataclass(frozen=True)
class OpenHandle:
    desired_access: int
    share_mode: int

def compatible(existing: OpenHandle, incoming: OpenHandle) -> bool:
    # Both directions matter: what the new open requests, and what it shares.
    requested_allowed_by_existing = (
        incoming.desired_access & ~existing.share_mode
    ) == 0
    existing_allowed_by_incoming = (
        existing.desired_access & ~incoming.share_mode
    ) == 0
    return requested_allowed_by_existing and existing_allowed_by_incoming

current = OpenHandle(desired_access=READ, share_mode=READ)
cases = [
    ("second reader", OpenHandle(READ, READ), True),
    ("new writer", OpenHandle(WRITE, READ), False),
    ("exclusive reader", OpenHandle(READ, 0), False),
    ("reader allowing writes", OpenHandle(READ, READ | WRITE), True),
    ("new delete request", OpenHandle(DELETE, READ | DELETE), False),
]
for title, request, expected in cases:
    actual = compatible(current, request)
    print(title, "->", "compatible" if actual else "sharing conflict")
    assert actual is expected

print("5/5 synthetic sharing checks passed; this is not a Win32 implementation.")
