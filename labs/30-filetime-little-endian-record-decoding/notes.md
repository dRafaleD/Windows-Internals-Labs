# Day 30 — FILETIME Little-Endian Record Decoding

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

Day 29 explored exact round trips and field-specific sentinel values. Now decode an invented eight-byte field using unsigned little-endian arithmetic. The Unix epoch is 116444736000000000 FILETIME ticks; its byte representation is 00 80 3e d5 de b1 9d 01. Preserve the sub-microsecond remainder and distinguish a field whose documented toy contract treats zero as missing from ordinary arithmetic zero. Practice: decode the hex by hand, reverse the byte order and inspect the difference, add a truncated field and verify it is rejected. Nine field cases plus three explicit checks. This is an offline arithmetic fixture, not a real NTFS parser; sentinel interpretation depends on the actual Windows field.

## Run
```bash
python3 labs/30-filetime-little-endian-record-decoding/lab.py
python3 test_all.py
```
