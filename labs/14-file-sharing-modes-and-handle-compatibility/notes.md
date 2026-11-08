# Day 14 — Windows File Sharing Modes and Handle Compatibility

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline lab](lab.py)

## Goal
Day 13 examined a file handle's granted access mask. Today we separate **desired access** from **share mode**: opening a file with read permission does not automatically mean other handles can also read or write it.

## Why two checks matter
When a Windows application opens a file, APIs such as `CreateFile` accept a **desired access** mask and **sharing flags**, including `FILE_SHARE_READ`, `FILE_SHARE_WRITE` and `FILE_SHARE_DELETE`. Sharing is a compatibility promise to other concurrent opens; it is not the same as a DACL or an ACL permission grant.

For simplified compatibility between an existing handle and a new one:
1. The new handle's desired access must be allowed by the **existing** handle's share flags.
2. The **existing** handle's desired access must be permitted by the new handle's share flags.

This is a teaching model. Real Windows checks involve more access rights, file objects, delete-pending state, leases and API subtleties. Never treat this simulation as a Windows kernel specification.

## Practice
```bash
python lab.py
```
A synthetic existing handle requests READ and shares READ. The example checks a second reader (allowed), a writer (denied by the existing share flags), and an exclusive new reader (denied because it refuses to share with the existing reader). It opens **no real file**.

## Exercises
1. Explain why a new reader with share mode `NONE` can fail even though it only asks to read.
2. Change the existing handle's share mode to `READ | WRITE`; which new requests may pass?
3. Contrast **file share compatibility** with **identity/DACL authorization**.
4. When troubleshooting a “sharing violation,” which process, path, timestamps and handle rights would you collect?
5. Identify one false assumption made by inferring file writes from an open handle alone.

## Safety and provenance
Pure Python with invented handles and no Win32 calls or file modifications. A compatible open does not prove any read or write happened.

## Documentation
- [Microsoft CreateFile function](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew)
- [Windows File Sharing](https://learn.microsoft.com/en-us/windows/win32/fileio/file-sharing)
