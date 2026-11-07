# Day 07 — NTFS File Metadata and Timestamp Uncertainty

[English](notes.md) · [Türkçe](notes.tr.md) · [Practice](lab.py)

## Objective and context

NTFS contains file metadata beyond filenames. Timestamps can aid timeline reconstruction, but file copying, backup tools, clock changes and filesystem semantics complicate interpretation.

## Technical concepts

1. Creation, modification, access and metadata-change timestamps are different concepts; availability and behavior depend on filesystem and API.

2. Python's portable stat fields do not expose every NTFS artifact, such as the complete MFT record, USN journal or alternate data streams.

3. Preserve originals, normalize time zones and record collection tools. Avoid declaring timestomping from one anomalous date.

## Case study

A training text file is created, changed and stat'ed. Record what can actually be observed through the portable API.

## Safe offline practical

Predict the expected results before running the Python 3 script:

```bash
python lab.py
```

The script uses synthetic fixtures, includes assertions, and never changes actual Windows settings.

## Optional Windows observation (read-only)

On your own Windows system, you may run this **read-only** PowerShell command. Record what it shows and any permissions limitations.

```powershell
Get-Item $env:TEMP | Select-Object FullName, CreationTimeUtc, LastWriteTimeUtc, LastAccessTimeUtc
```

This observation is separate from the Python model; results depend on OS version and privileges.

## Assignments

1. Observe mtime and size before and after modifying the temporary file.
2. Distinguish st_ctime semantics on Windows versus Unix.
3. Name NTFS artifacts not extracted by this demo.

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
