# Day 04 — Virtual Memory Regions, Pages and Protection

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Processes work with virtual addresses. Memory managers map regions and page protections; the virtual address is not itself a raw physical RAM location.

## Technical concepts

1. Reserve and commit are distinct concepts in Windows memory management. A reserved region is not automatically committed usable storage.

2. Page permissions such as read, write and execute control operations and influence vulnerability impact; W^X is a defensive design goal, not universal system behavior.

3. A memory map snapshot can change quickly and does not reveal every past allocation or access.

## Case study

A synthetic page requests both write and execute. Flag it for review, not as confirmed malware.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Process | Select-Object -First 8 Name, Id, VirtualMemorySize64, WorkingSet64
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Classify reserve-only and committed regions.
2. Find W+X pages and explain false positives.
3. Suggest evidence beyond memory permissions.

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
