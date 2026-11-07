"""Toy virtual-memory region table. No allocation or API calls."""
regions = [
    {"base":"0x1000", "state":"reserved", "permissions":""},
    {"base":"0x2000", "state":"committed", "permissions":"R"},
    {"base":"0x3000", "state":"committed", "permissions":"RX"},
    {"base":"0x4000", "state":"committed", "permissions":"RWX"},
]
def runnable(region):
    return region["state"] == "committed" and "X" in region["permissions"]
warnings = [r["base"] for r in regions if
            r["state"] == "committed" and
            "W" in r["permissions"] and "X" in r["permissions"]]
assert warnings == ["0x4000"]
assert not runnable(regions[0])
print("Review (not malware verdict):", warnings)
