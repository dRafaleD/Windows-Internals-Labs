# Day 32 — FILETIME Exact Deltas and Clock Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

Day 31 reconstructed FILETIME ticks from high and low words. Today subtract exact integers first, then express the signed difference in seconds as a Fraction. Adjacent ticks differ by 100 ns even when both timestamps round to the same Python microsecond. Supplied uncertainty bounds are expressed in ticks; overlapping intervals prevent a definite ordering. Eleven examples include one tick, negative differences, one second, touching intervals and invalid unsigned inputs. Practice: compare 10 and 11 ticks with uncertainty of five ticks on each observation. Explain why timestamp resolution is not clock accuracy. This only models invented arithmetic values; actual Windows sentinel semantics and clock provenance must be assessed separately.

## Run
```bash
python3 labs/32-filetime-exact-deltas-and-clock-ambiguity/lab.py
python3 test_all.py
```
