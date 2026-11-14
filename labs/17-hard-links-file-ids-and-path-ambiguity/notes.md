# Day 17 — Hard Links, File IDs and Path Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Day 16 follow-up
A rename can change a path while an open handle keeps referring to the same file. **Hard links** introduce another wrinkle: two different filenames can name the **same file object** simultaneously.

Our toy map associates two paths with file ID 100. After unlinking one name, the other still points to the object. After unlinking both names, an open handle still keeps the modeled object alive. Reusing the old pathname for ID 101 does **not** make ID 101 the original file.

## Run
```bash
python3 labs/17-hard-links-file-ids-and-path-ambiguity/lab.py
python3 test_all.py
```

## Investigation tasks
Why can two paths represent the same object? How would hard links distort a path-only forensic timeline? Why should identity be scoped to its volume? What changes when one name is unlinked but handles remain?

## Limits
In-memory teaching abstraction, not an emulation of NTFS, Win32 APIs, permissions, filesystem reference counting, reparse points or delete-sharing behavior. No real file is changed.
