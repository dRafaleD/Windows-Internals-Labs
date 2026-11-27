# Day 31 — FILETIME High/Low Word Reconstruction

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

Day 30 decoded little-endian FILETIME bytes. Today reconstruct the integer from the low and high unsigned 32-bit words. The high word is shifted by 32 bits, then combined with the low word. Worked boundary: low=0xffffffff, high=0 gives 4294967295; low=0, high=1 gives 4294967296. Seven round-trip values and seven invalid cases exercise boundaries. Calculate the two Unix epoch words, then compare their little-endian serialization. Swapping words changes the value. This is integer representation only, not interpretation of a real Windows field; no Windows APIs or disk access.

## Run
```bash
python3 labs/31-filetime-high-low-word-reconstruction/lab.py
python3 test_all.py
```
