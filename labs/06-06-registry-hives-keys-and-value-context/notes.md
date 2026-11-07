# Day 06 — Registry Hives, Keys and Value Context

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

The Windows Registry stores structured configuration. A key's location, value type and owner matter when interpreting a change; mere existence does not prove persistence or malicious behavior.

## Technical concepts

1. Common root hives include HKLM and HKCU; per-user and machine-wide settings affect different scopes.

2. Run/RunOnce values may be relevant to startup analysis, but legitimate applications also use them. Correlate path, signature, change time and execution.

3. Registry views can differ on 32-bit and 64-bit Windows; avoid hardcoded assumptions about where software is registered.

## Case study

A synthetic startup key contains a legitimate updater and an unknown-looking path. Classify findings as review candidates, not definitive threat labels.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-ItemProperty 'HKCU:\Software\Microsoft\Windows\CurrentVersion\Run' -ErrorAction SilentlyContinue
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Compare user and machine hives in the fixture.
2. Add a benign startup entry and re-evaluate.
3. Explain what evidence could establish actual execution.

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
