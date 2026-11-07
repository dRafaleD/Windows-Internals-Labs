"""Parse only minimal PE markers in in-memory synthetic bytes; never execute files."""
import struct

def parse_markers(data):
    if len(data) < 0x40 or data[:2] != b"MZ":
        raise ValueError("Missing DOS header")
    pe_offset = struct.unpack_from("<I", data, 0x3c)[0]
    if pe_offset > len(data) - 24:
        raise ValueError("PE/COFF header out of bounds")
    if data[pe_offset:pe_offset+4] != b"PE\x00\x00":
        raise ValueError("Bad PE signature")
    machine, sections = struct.unpack_from("<HH", data, pe_offset + 4)
    return machine, sections

fixture = bytearray(128)
fixture[:2] = b"MZ"
struct.pack_into("<I", fixture, 0x3c, 64)
fixture[64:68] = b"PE\x00\x00"
struct.pack_into("<HH", fixture, 68, 0x8664, 1)
assert parse_markers(fixture) == (0x8664, 1)
for invalid in [bytes(fixture[:70]), bytes(b"XX"+fixture[2:])]:
    try:
        parse_markers(invalid)
    except ValueError:
        print("Rejected malformed fixture")
    else:
        raise AssertionError("Malformed input accepted")
print("Toy PE marker checks passed; not a full PE validator.")
