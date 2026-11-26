# Day 29 — FILETIME Exact Round Trips and Sentinel Values

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

Day 28 converted FILETIME ticks while preserving the sub-microsecond remainder. Day 29 verifies lossless round trips: decode to UTC datetime plus a remainder from 0 to 9, then encode using integer arithmetic. No floating-point Unix timestamp conversion is needed.

A zero value may be treated as the 1601 base in an arithmetic exercise or as missing if a particular field specification says so. The fictional zero_is_missing policy illustrates that context; it is not a universal Windows rule.

**Practice:** predict the remainder for OFFSET+7 and OFFSET-1, test the round trips, and compare decoding zero with both policies. Explain why numeric precision does not prove timestamp accuracy. Nine round trips and nine boundary checks. No Windows API or real artifacts; Python datetime has a smaller representable range than unsigned 64-bit FILETIME.

## Run
```bash
python3 labs/29-filetime-exact-roundtrips-and-sentinel-values/lab.py
python3 test_all.py
```
