# Windows Internals Labs

[🇬🇧 English](README.md) · [🇹🇷 Türkçe](README.tr.md)

A **12-day bilingual, beginner-friendly practical series** covering Windows processes, threads, PE files, memory, Registry, access controls, Event Logs and ETW/Sysmon.

## Labs

| Day | Topic | Notes | Practice |
| --- | --- | --- | --- |
| 01 | Windows Processes, PIDs and Parent-Child Trees | [English](labs/01-processes-pids-and-parent-child-trees/notes.md) · [Türkçe](labs/01-processes-pids-and-parent-child-trees/notes.tr.md) | [lab.py](labs/01-processes-pids-and-parent-child-trees/lab.py) |
| 02 | Threads, Handles and Object Lifetime | [English](labs/02-threads-handles-and-lifetime/notes.md) · [Türkçe](labs/02-threads-handles-and-lifetime/notes.tr.md) | [lab.py](labs/02-threads-handles-and-lifetime/lab.py) |
| 03 | PE Headers, Machine Types and Safe Parsing | [English](labs/03-pe-headers-and-machine-types/notes.md) · [Türkçe](labs/03-pe-headers-and-machine-types/notes.tr.md) | [lab.py](labs/03-pe-headers-and-machine-types/lab.py) |
| 04 | Virtual Memory Regions, Pages and Protection | [English](labs/04-virtual-memory-regions-and-page-protection/notes.md) · [Türkçe](labs/04-virtual-memory-regions-and-page-protection/notes.tr.md) | [lab.py](labs/04-virtual-memory-regions-and-page-protection/lab.py) |
| 05 | DLL Loading, Search Paths and Trust Boundaries | [English](labs/05-dll-loading-paths-and-search-boundaries/notes.md) · [Türkçe](labs/05-dll-loading-paths-and-search-boundaries/notes.tr.md) | [lab.py](labs/05-dll-loading-paths-and-search-boundaries/lab.py) |
| 06 | Registry Hives, Keys and Value Context | [English](labs/06-registry-hives-keys-and-value-context/notes.md) · [Türkçe](labs/06-registry-hives-keys-and-value-context/notes.tr.md) | [lab.py](labs/06-registry-hives-keys-and-value-context/lab.py) |
| 07 | NTFS File Metadata and Timestamp Uncertainty | [English](labs/07-ntfs-file-metadata-and-time-uncertainty/notes.md) · [Türkçe](labs/07-ntfs-file-metadata-and-time-uncertainty/notes.tr.md) | [lab.py](labs/07-ntfs-file-metadata-and-time-uncertainty/lab.py) |
| 08 | Access Tokens, SIDs and DACL Evaluation | [English](labs/08-access-tokens-sids-and-dacl-models/notes.md) · [Türkçe](labs/08-access-tokens-sids-and-dacl-models/notes.tr.md) | [lab.py](labs/08-access-tokens-sids-and-dacl-models/lab.py) |
| 09 | Windows Event Logs, Providers and Event IDs | [English](labs/09-windows-event-logs-and-provider-context/notes.md) · [Türkçe](labs/09-windows-event-logs-and-provider-context/notes.tr.md) | [lab.py](labs/09-windows-event-logs-and-provider-context/lab.py) |
| 10 | Services, Scheduled Tasks and Startup Context | [English](labs/10-windows-services-and-scheduled-tasks/notes.md) · [Türkçe](labs/10-windows-services-and-scheduled-tasks/notes.tr.md) | [lab.py](labs/10-windows-services-and-scheduled-tasks/lab.py) |
| 11 | ETW, Sysmon and Process Event Correlation | [English](labs/11-etw-sysmon-and-process-event-correlation/notes.md) · [Türkçe](labs/11-etw-sysmon-and-process-event-correlation/notes.tr.md) | [lab.py](labs/11-etw-sysmon-and-process-event-correlation/lab.py) |
| 12 | Windows Internals Evidence Reconstruction Capstone | [English](labs/12-windows-internals-evidence-capstone/notes.md) · [Türkçe](labs/12-windows-internals-evidence-capstone/notes.tr.md) | [lab.py](labs/12-windows-internals-evidence-capstone/lab.py) |

## How to study

1. Read the notes in either language and compare the terminology.
2. Inspect the Python script and predict its output.
3. Run `python lab.py` and observe the assertions. Run `python test_all.py` at the repo root to smoke-check all 12 labs.
4. Optionally run the read-only PowerShell command on your own Windows machine.
5. Document a false positive and a missing-evidence scenario.

## Requirements

- Python 3.10+ (standard library; most labs run cross-platform)
- Optional: Windows 10/11 with PowerShell 5.1+ for read-only observations.
- Start without administrator access; some Windows event channels and metadata may be restricted.

## Structure

```text
Windows-Internals-Labs/
├── README.md
├── README.tr.md
├── resources.md
└── labs/
    ├── 01-processes-pids-and-parent-child-trees/
    │   ├── notes.md
    │   ├── notes.tr.md
    │   └── lab.py
    └── ... (12 days with the same structure)
```

## Limits and safety

Examples do not read live process memory, load DLLs, modify Registry values or clear logs. Python models intentionally simplify real kernel behavior. Inspect only systems you own or are authorized to examine.

## Next steps

After the core 12 days, continue with WinDbg, deeper PE loader mechanics, memory forensics, Win32 API and controlled ETW exercises.

