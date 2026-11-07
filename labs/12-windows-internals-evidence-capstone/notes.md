# Day 12 — Windows Internals Evidence Reconstruction Capstone

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Reconstruct a small Windows-like activity sequence from independent synthetic process, file and event records. Clearly separate direct observations from attribution and intent.

## Technical concepts

1. Build a UTC timeline with source IDs, provider information and stable correlation keys. Preserve the original records.

2. A file appearing after a process started does not, by itself, prove that process created the file; an independent file-operation log is needed.

3. Report missing logs, time-resolution limits and contradictions. Incomplete evidence may warrant an inconclusive finding.

## Case study

A synthetic process is created and a file event appears one minute later. Correlate them by process GUID, then document uncertainty about who initiated the process.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Date -Format o; Get-CimInstance Win32_OperatingSystem | Select-Object Caption, Version, BuildNumber
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Run the mini investigation and inspect source-preserving timeline.
2. Create a short report: observations, hypotheses, missing evidence and confidence.
3. Suggest additional benign tests before drawing an actor-attribution conclusion.

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
