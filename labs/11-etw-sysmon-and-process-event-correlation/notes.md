# Day 11 — ETW, Sysmon and Process Event Correlation

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Event Tracing for Windows (ETW) and tools such as Sysmon can provide process and image activity context. Correlation needs identifiers and time bounds, not only matching process names.

## Technical concepts

1. Sysmon Event ID 1 commonly records process creation when configured; event availability depends on installed configuration and collection.

2. Process GUIDs can be more useful than PIDs for cross-event correlation, but source schemas and GUID provenance should still be validated.

3. A name match is weak evidence. Use event ID, provider, creation time, image path and parent identifiers when available.

## Case study

An event stream contains two processes with the same name but distinct GUIDs. Correlate activity to the correct process.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Service Sysmon64,Sysmon -ErrorAction SilentlyContinue | Select-Object Name, Status
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Join records on the synthetic process GUID.
2. Demonstrate why joining only on image name is ambiguous.
3. Identify missing telemetry that would limit a real investigation.

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
