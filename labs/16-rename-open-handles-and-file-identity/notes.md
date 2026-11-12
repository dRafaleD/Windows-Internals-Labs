# Day 16 — Rename Operations, Open Handles and File Identity

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline exercise](lab.py)

## Link to Day 15
Day 15 modeled delete-pending status and `FILE_SHARE_DELETE`. Day 16 explores another effect of open handles: **renaming a file can change its path while an existing handle continues referring to the same file object**.

**Handle:** an open reference to a kernel-managed resource. **File identity:** the underlying object, which may outlive one pathname. **Share mode:** permissions for how other opens can coexist with the current open. **DELETE access:** an access right that is relevant to rename/delete operations. Having a share flag is **not** itself authorization to rename.

## Synthetic rules
A `Model` maps paths to fictional numeric file IDs, and each file tracks open handles.

An illustrative rename succeeds only when:
1. The old path exists and the new path does not already exist.
2. The caller is explicitly marked as having deletion/rename access.
3. Every currently open handle permits `DELETE` in its share mode.

If successful, the path map changes but `file_id` and existing handles do not. This helps distinguish path-based evidence from object-based evidence. Existing handles do not become references to a different object merely because a path changes.

## Run offline
~~~bash
python3 labs/16-rename-open-handles-and-file-identity/lab.py
python3 test_all.py
~~~
The repository-wide smoke runner now includes all 16 labs.

## Investigation questions
1. Why might a process keep reading data after a filename changes?
2. Why does `FILE_SHARE_DELETE` not authorize rename on its own?
3. Which checks should reject a rename to an existing path?
4. Why are file ID, path and handle three different fields in a forensic record?
5. How do hard links, reparse points, different filesystems, ACLs and real Win32 rename semantics complicate this model?

## Limits
This is **not** an emulator of Windows file sharing rules or `MoveFileEx`, `SetFileInformationByHandle` or POSIX rename. Real behavior depends on access checks, filesystem, flags and sharing semantics. No actual files are touched.
