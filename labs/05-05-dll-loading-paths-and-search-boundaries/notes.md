# Day 05 — DLL Loading, Search Paths and Trust Boundaries

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Programs dynamically load libraries. Ambiguous, relative or name-only DLL references can increase the importance of the load context and filesystem permissions.

## Technical concepts

1. Exact Windows DLL search rules depend on API, loader settings, packaged app status and system mitigations; do not assume one universal directory order.

2. Prefer fully qualified paths and trusted application locations where suitable; verify library signatures and update processes independently.

3. A library present on a path does not prove it was loaded or that its code executed. Investigations need module-load evidence.

## Case study

A synthetic application passes 'example.dll' as a relative name. The exercise checks whether a simulated load request specifies a trusted absolute path.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Process -Id $PID | Select-Object Name, Id, Path
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Compare fully qualified and relative DLL names.
2. Discuss why file presence and module load are different observations.
3. List documentation and telemetry needed for a real Windows analysis.

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
