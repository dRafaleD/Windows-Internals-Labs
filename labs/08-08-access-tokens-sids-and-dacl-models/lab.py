"""Simplified SID/group policy: NOT Windows Authz or AccessCheck."""
aces = [
    {"effect":"allow", "identity":"Readers", "right":"read"},
    {"effect":"deny", "identity":"Guest", "right":"read"},
]
def can_read(identities):
    matches = [a for a in aces if a["identity"] in identities and a["right"] == "read"]
    return not any(a["effect"] == "deny" for a in matches) and any(a["effect"] == "allow" for a in matches)
assert can_read({"UserA","Readers"})
assert not can_read({"Guest","Readers"})
assert not can_read({"Nobody"})
print("Toy ACL evaluation checks passed; Windows security semantics are more detailed.")
