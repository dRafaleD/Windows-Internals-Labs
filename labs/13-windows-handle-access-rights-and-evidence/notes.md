# Day 13 — Windows Handle Access Rights and Evidence

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Learning objective

Learn the trust and evidence boundaries of **Windows Handle Access Rights and Evidence** using harmless local fixtures.

## Core concepts

1. Windows handles are process-local references; the granted access mask helps describe permitted operations on the referenced object.

2. Requested access and granted access can differ. A mask should be decoded with object-type-specific rights and appropriate Windows APIs.

3. A process holding a handle does not prove it actually used all granted permissions. This demo does not inspect real process handles.

## Safe hands-on

Read the code and predict its output before running:

```bash
python lab.py
```

Output is synthetic; no operations are sent to a live target.

## Assignments

1. Identify input provenance and untrusted fields.
2. Add and test a negative or boundary case.
3. Separate direct observations from interpretations.
4. Describe additional validation needed in a real environment.

## Knowledge check

- Is any single indicator sufficient?
- What can cause false positives or missing evidence?
- What inputs are needed to reproduce the result?

## Safety and limitations

No live malware, cloud accounts, system modifications, or outbound traffic. This minimal model is not an exact platform implementation.
