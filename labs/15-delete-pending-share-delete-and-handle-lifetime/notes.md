# Day 15 — Delete-Pending, FILE_SHARE_DELETE and Handle Lifetime

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline simulation](lab.py)

## Learning goal
Day 14 distinguished **desired access** from **file share mode**. A compatible open is not the same as permission to modify or delete a file. Day 15 extends this with a simplified **delete-pending** lifecycle: how existing handles can prevent deletion and why requesting deletion does not necessarily make a file disappear immediately.

## The three separate questions
1. **Access authorization:** Does the caller have permission to request deletion? Windows access checks, granted DELETE rights and filesystem rules matter. Our fixture represents this with a single `caller_authorized` boolean—*not* a real security token or DACL check.
2. **Sharing compatibility:** If an existing open handle omitted `FILE_SHARE_DELETE`, a new delete-related operation may fail with a sharing conflict. `FILE_SHARE_DELETE` is **permission to coexist with certain operations**, not a grant to delete the file.
3. **Object lifetime:** Under a simplified traditional deletion model, a successful delete request marks the file **delete-pending** while handles remain open; after the last handle closes, deletion completes. New opens are rejected while pending *in this teaching model*.

Real Windows behavior depends on the exact API, disposition flags, file system, delete-on-close/POSIX semantics and active references. Do not treat this state machine as an exact NT kernel specification.

## Practical: all fake handles, no filesystem changes
Run from this folder:
```bash
python lab.py
```
The Python standard-library script tests:
- A reader that **did not** share DELETE: an authorized delete request is rejected.
- Readers that **did** share DELETE: the controller still rejects a caller without delete authorization.
- An authorized request sets `delete_pending`. A new open is refused.
- Closing one handle does not finish deletion; closing the final handle does in the model.

Assertions check each outcome. The script never invokes Win32 APIs, opens real files, modifies ACLs or deletes anything.

## Questions and exercises
1. Why does `FILE_SHARE_DELETE` not mean “this process is allowed to delete the file”?
2. Which denial is caused by **access authorization**, and which by **sharing compatibility**?
3. Explain why a **delete-pending** observation is not proof the bytes have already been physically erased.
4. Add a third open handle whose share mode lacks DELETE. Predict and test the request result.
5. Model a caller that has permission to read but not delete. What evidence would establish granted rights on a real handle?
6. For an authorized forensic investigation, which handle IDs, process IDs, paths, access masks and timestamps would you record? What can be inferred versus observed?

## Limitations and documentation
This is a deterministic educational model, not Windows API testing. Production behavior includes different create dispositions, rename/delete semantics, security checks, handle duplicates, section objects and sharing edge cases. Consult [CreateFileW](https://learn.microsoft.com/en-us/windows/win32/api/fileapi/nf-fileapi-createfilew) and [File Sharing](https://learn.microsoft.com/en-us/windows/win32/fileio/file-sharing) for the supported Windows semantics. Always use only owned or authorized systems.
