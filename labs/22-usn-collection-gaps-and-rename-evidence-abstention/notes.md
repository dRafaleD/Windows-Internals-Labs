# Day 22 — USN Collection Gaps and Rename-Evidence Abstention

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## After Day 21
Day 21 treated NTFS rename reasons as **bit flags**, and returned **AMBIGUOUS** if multiple old-name records could match one new-name record. Day 22 adds a crucial forensic issue: **collection completeness**.

## Model
The synthetic examiner knows about explicit intervals where journal records were **not acquired**. These are recorded as `unavailable_ranges` and **must not be inferred from gaps between numeric USN values**. Real NTFS USN values are not simple consecutive row numbers.

For a possible old-name/new-name pair sharing volume, file ID and *invented toy epoch*:
- **PAIR_CANDIDATE:** one matching older record, and no known collection gap between it and the new record.
- **UNCERTAIN_GAP:** one candidate, but a known unavailable acquisition range may hide alternatives.
- **AMBIGUOUS:** two or more candidate records.
- **INSUFFICIENT:** no candidate or missing necessary reason/identity evidence.

## Run
```bash
python3 labs/22-usn-collection-gaps-and-rename-evidence-abstention/lab.py
python3 test_all.py
```

## Questions
1. Why can a missing collection interval make a seemingly unique pairing uncertain?
2. Why is an arbitrary difference between two USN numbers **not** evidence of missing events?
3. What is the distinction between a rename candidate and a proven rename?
4. How does numeric file-reference reuse affect a reconstructed timeline?
5. What acquisition metadata could validate coverage?

## Limits
All reason-bit positions and `toy_epoch` are invented. This is not a real USN Journal parser, NTFS reference implementation or actor attribution tool.
