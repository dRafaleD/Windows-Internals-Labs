# Day 21 — USN Bit Flags and Ambiguous Rename Pairs

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## After Day 20
Day 20 paired fictional `RENAME_OLD_NAME` and `RENAME_NEW_NAME` records when their file reference and order matched. Day 21 adds two realities of forensic triage: **reason flags can coexist** and **multiple candidate old-name records can make a pairing ambiguous**.

## Model
Each invented record has a volume, numeric file ID, **toy epoch**, USN value, a bitmask reason and name. The old-name requirement is checked using `reason & OLD_NAME`, so a record with `OLD_NAME | CLOSE` is accepted. A new-name record may likewise include multiple flags.

Potential old-name candidates must share the modeled identity and precede the new event within a short illustrative USN gap:
- **PAIR_CANDIDATE:** exactly one old-name candidate.
- **AMBIGUOUS:** more than one candidate; do not arbitrarily select one.
- **INSUFFICIENT:** no candidate or invalid contextual match.

## Reproduce
~~~bash
python3 labs/21-usn-bitflags-and-ambiguous-rename-pairs/lab.py
python3 test_all.py
~~~

## Crucial limits
The reason bit positions and `toy_epoch` are **invented**, not actual NTFS constant definitions or a guaranteed Windows field. Real USN parsing must account for journal version, record layout, actual flags, file reference sequences, incomplete acquisition and record wraparound. A matching pair does not establish actor identity or a complete rename timeline.

## Exercises
1. Why is a bit test better than equality to a single reason flag?
2. Why should two old-name candidates yield `AMBIGUOUS`?
3. What does an incomplete USN journal do to the search?
4. Why must file identity be interpreted within volume and time context?
5. What additional process and handle evidence could support a rename hypothesis?

## Safety
Cross-platform Python with synthetic data only; no Windows API, file deletion or registry access.
