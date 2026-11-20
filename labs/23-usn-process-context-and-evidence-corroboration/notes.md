# Day 23 — USN Process Context and Evidence Corroboration

[English](notes.md) · [Türkçe](notes.tr.md) · [Python exercise](lab.py)

## From Day 22
Day 22 identified **known USN collection gaps** that make rename pairing uncertain. Today we add a *different kind* of evidence: fictional **process telemetry** recorded near a possible rename event.

## Correlation policy
A possible old-name/new-name pair must share volume, numeric file ID and an **invented toy epoch**, with increasing USN values. The algorithm first checks ambiguous old-name candidates and acquisition gaps.

Only after that does it correlate recorded `RENAME` process context with the same toy identity and a ±2-second proximity window:
- **PAIR_ONLY:** plausible USN name pair without process context.
- **PAIR_WITH_CONTEXT:** one matching process-context observation.
- **AMBIGUOUS_PROCESS_CONTEXT:** multiple different candidate process GUIDs.
- **UNCERTAIN_COLLECTION / AMBIGUOUS_OLD_NAME / INSUFFICIENT:** report limited evidence rather than inventing a causal explanation.

## Run
```bash
python3 labs/23-usn-process-context-and-evidence-corroboration/lab.py
python3 test_all.py
```

## Critical caveats
The reason flags and `toy_epoch` are **invented**, not actual NTFS or Sysmon field definitions. Real event sources have different timestamp provenance, identity fields and collection gaps. A correlated process record is **not proof** that a named human initiated the rename.

## Questions
1. Why must collection completeness be considered before attributing a rename?
2. Why is a nearby process event contextual evidence rather than proof?
3. How could two processes match the same time window?
4. How should file-ID reuse and timestamp uncertainty be reported?
5. What actual USN and process events would an examiner corroborate?

## Safety
No real Windows data, filesystem manipulation, registry access or live event collection.
