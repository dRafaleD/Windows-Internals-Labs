# Day 10 — Services, Scheduled Tasks and Startup Context

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

Windows services and scheduled tasks support legitimate background work. Their configuration, triggers and execution accounts matter in reliability and security reviews.

## Technical concepts

1. A service configuration describes how a service may run; it does not prove it actually executed during the investigated window.

2. Scheduled tasks can trigger on time, event or user actions. Inspect trigger, action, principal and task history together.

3. New startup entries are review signals rather than automatic malware indicators; use a baseline and authorized configuration data.

## Case study

A synthetic scheduled task unexpectedly points to a temporary folder; flag the configuration for review without running it.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Service | Select-Object -First 6 Name, Status, StartType; Get-ScheduledTask | Select-Object -First 6 TaskName, State
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Compare a safe baseline against current synthetic task definitions.
2. Explain difference between task presence and execution.
3. Discuss appropriate logging and evidence.

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
