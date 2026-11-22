# Day 25 — USN Rename and MFT Snapshot Identity Checks

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## From Day 24
An interval-aware match between a process event and a USN rename can still be ambiguous. Day 25 adds **MFT snapshots** and tests whether observations of the file's identity and name are internally consistent with a possible rename pair.

## Evidence model
A fictional USN old-name/new-name pair carries **volume, file index, sequence, USN value, timestamp and name**. Two fictional MFT snapshots show the file before and after the renamed state. The model asks:
1. Does the old event precede the new event, with matching file reference and volume?
2. Is a known USN collection gap present?
3. Do MFT snapshots reference the **same sequence** and expected file index?
4. Do their observed names and collection times fit the proposed rename?

The outcomes distinguish `CONSISTENT_CANDIDATE`, `FILE_REFERENCE_REUSE`, `UNCERTAIN_COLLECTION`, timing conflicts, identity conflicts and missing snapshots.

## Run
```bash
python3 labs/25-usn-rename-and-mft-snapshot-identity-checks/lab.py
python3 test_all.py
```

## Critical caveats
These are **invented records**, not a real parser for NTFS $MFT or $UsnJrnl. Real file reference numbers, sequence values, renamed-name retention, snapshot times and USN record structures have additional semantics. An MFT snapshot records observed **state at collection**, not an authoritative event-by-event history. A consistent candidate is not proof of the initiating process or person.

## Questions
What does file-reference reuse do to filename correlation? Why is a later MFT name only supporting context? How can a gap in acquired USN records weaken a plausible pair? Which separate sources would you use to corroborate the rename?
