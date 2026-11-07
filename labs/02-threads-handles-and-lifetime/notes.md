# Day 02 — Threads, Handles and Object Lifetime

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Threads execute instructions inside a process. Handles are process-specific references to kernel-managed objects. A number that looks like a handle is not a transferable global identity.

## Technical concepts

1. A process may contain multiple threads sharing its address space; individual threads have separate execution context and stacks.

2. Closing a handle releases that process's reference; object lifetime depends on all remaining references and operating-system rules.

3. Handle values can be recycled. For investigations, record process identity, object type, access rights and collection time.

## Case study

Two processes use the same numeric handle value for different synthetic objects. Avoid treating the handles as identical objects.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Process | Select-Object -First 8 Name, Id, Threads, HandleCount
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Compare handle identity using (process, value) pairs.
2. Simulate close and reopen with the same numeric value.
3. Explain why a live handle listing may be incomplete.

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
