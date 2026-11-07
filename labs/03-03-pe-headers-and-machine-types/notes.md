# Day 03 — PE Headers, Machine Types and Safe Parsing

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

The Windows Portable Executable (PE) format contains a DOS header, a PE signature and COFF/optional header structures. Validate offsets and bounds before interpreting any untrusted bytes.

## Technical concepts

1. The DOS 'MZ' signature is at file offset 0. The little-endian e_lfanew field at 0x3c points toward the PE signature in common PE files.

2. The PE signature is four bytes: 'PE' followed by two NUL bytes. The following COFF header includes a machine type.

3. A signature alone does not prove the file is valid, executable or benign. A real parser must validate all relevant structure lengths and relationships.

## Case study

A sample claims to be PE but has e_lfanew pointing beyond end of file. Reject it safely.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Item $env:SystemRoot\System32\notepad.exe | Select-Object Name, Length, LastWriteTime
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Run the parser with valid and truncated synthetic buffers.
2. Add a wrong-MZ negative test.
3. Discuss which PE structures are omitted from this demo.

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
