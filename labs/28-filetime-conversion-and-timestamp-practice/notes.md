# Day 28 — Practice Day: FILETIME Conversion and Timestamp Interpretation

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

FILETIME represents elapsed 100-nanosecond intervals since 1601-01-01 UTC. Python datetime supports microseconds, so retain the remainder of division by ten rather than silently pretending that all seven decimal places were preserved.

| Input ticks | Expected |
|---|---|
| 0 | 1601-01-01 UTC (arithmetic interpretation only) |
| 1 | Base plus 100 ns, remainder 1 |
| 10 | Base plus 1 microsecond |
| 116444736000000000 | Unix epoch |
| Unix offset + 10000000 | Unix epoch + 1 second |
| Negative integer | INVALID_TICKS |
| Maximum unsigned 64-bit | OUT_OF_RANGE for Python datetime |

**Exercises:** Convert one second and one millisecond into ticks. Predict the 13 decode cases; compare 00:00 UTC and 03:00 +03:00. Reconstruct an exact tick count using the microsecond-level datetime plus remainder. Explain the distinction between timestamp precision and event accuracy.

Expected summary: 13 decode cases + 5 encode checks passed. No real NTFS records or Windows API. Some Windows structures assign special meanings to zero or other values; this is arithmetic conversion, not interpretation of all Windows timestamp fields.

## Run
```bash
python3 labs/28-filetime-conversion-and-timestamp-practice/lab.py
python3 test_all.py
```
