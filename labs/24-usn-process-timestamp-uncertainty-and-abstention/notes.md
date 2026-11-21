# Day 24 — USN/Process Timestamp Uncertainty and Abstention

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## From Day 23
Day 23 looked for a process event within **±2 seconds** of a possible USN rename. Real timestamps have uncertainty from clock offsets, event-generation delay, filesystem resolution and collection timing. A strict numeric threshold may therefore conceal plausible matches or create unjustified certainty.

## Interval-aware correlation
Each fictional USN/process event has `time ± uncertainty`. A process observation is a **possible contextual match** if its earliest/latest possible interval is within a two-second allowance of the rename event's interval, and the toy volume, file ID and epoch match.

The classifier distinguishes **PAIR_WITH_POSSIBLE_CONTEXT**, **PAIR_ONLY**, **AMBIGUOUS_CONTEXT**, **UNCERTAIN_COLLECTION**, **AMBIGUOUS_OLD_NAME** and **INSUFFICIENT**. Negative uncertainty is rejected. A known acquisition gap takes precedence over contextual claims.

## Run
```bash
python3 labs/24-usn-process-timestamp-uncertainty-and-abstention/lab.py
python3 test_all.py
```

## Forensic cautions
The reason bits and `toy_epoch` are **invented**, not actual Windows constants or guaranteed NTFS fields. Actual USN changes and process telemetry need documented clocks, record versions, source provenance and acquisition coverage. Equal-looking identities and time overlap never prove a process or human initiated the operation.

## Questions
1. Why is a timestamp an interval rather than an exact event moment?
2. How does collector clock skew change possible correlation?
3. Why should two possible process GUIDs produce an ambiguous result?
4. What does a known USN collection gap do to the conclusion?
5. What separate records could support an initiator hypothesis?

## Limits
No Windows system, disk, Registry or journal is accessed. All cases are harmless synthetic evidence.
