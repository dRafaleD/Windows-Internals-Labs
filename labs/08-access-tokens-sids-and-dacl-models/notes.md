# Day 08 — Access Tokens, SIDs and DACL Evaluation

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Windows uses security identifiers (SIDs), tokens and access control lists to express identity and resource permissions. Access-check order and inheritance need careful interpretation.

## Technical concepts

1. A token contains identity and group information plus privileges. Being in a group does not mean every privileged action is available in every context.

2. DACLs contain Access Control Entries (ACEs); actual Windows access-check behavior includes ordering, object types, inheritance and token details.

3. The lab's simplified explicit-deny-first model is pedagogical only and must not be mistaken for the Windows security reference monitor.

## Case study

A guest user belongs to the Readers group but also matches an explicit deny entry. Confirm the simplified policy denies read.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Acl $env:TEMP | Select-Object -ExpandProperty Access | Select-Object -First 8
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Evaluate a guest and normal reader.
2. Change one ACE and observe effective permission.
3. Explain why inherited and ordered ACEs complicate the full model.

## Knowledge check

1. What source produced this observation?
2. What does the record show, and what does it **not prove**?
3. What negative case could weaken your inference?
4. How would Windows version, configuration and collection time affect it?

## Safety and limitations

This is a defensive educational exercise. No production files, Registry entries, services or security settings are changed. `lab.py` is a **teaching simplification**, not a Windows kernel emulator or forensic collector.

## References

- [Microsoft Windows documentation](https://learn.microsoft.com/en-us/windows/win32/)
- [Windows Internals resources](https://learn.microsoft.com/en-us/sysinternals/)
