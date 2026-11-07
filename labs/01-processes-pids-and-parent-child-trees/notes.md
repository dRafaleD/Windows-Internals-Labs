# Day 01 — Windows Processes, PIDs and Parent-Child Trees

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

A process is an execution container with an address space, threads and operating-system-managed resources. Process trees give useful context but parent relationships alone do not establish maliciousness.

## Technical concepts

1. PID identifies a process at a moment in time, but identifiers can be reused after a process exits.

2. A parent process may have exited before collection; a missing parent can be normal. Timestamps and stable identifiers improve correlation.

3. The process tree is a partial view: command-line arguments, executable path, token and image signature require independent collection and verification.

## Case study

A synthetic helper process has a parent that was not captured. Report the missing link without calling it malware.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-CimInstance Win32_Process | Select-Object -First 8 ProcessId, ParentProcessId, Name
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Print the process tree and identify an orphan-like record.
2. Change one parent value and explain the result.
3. Discuss PID reuse and process start times.

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
