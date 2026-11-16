# Day 19 — File Identity Reuse and Event Correlation

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Connection to Day 18
Day 18 demonstrated numeric file-ID reuse after all toy links and handles disappeared. This lab asks how a forensic timeline might **incorrectly merge separate objects** when the same numeric ID or pathname appears again.

## Evidence dimensions
The fictional `Evidence` record has volume, numeric file ID, toy epoch, path, content digest and observation time. The classifier distinguishes:
- **SAME_TOY_OBJECT:** volume, ID and toy epoch all match, even after a rename.
- **REUSED_NUMERIC_ID:** same volume and numeric ID but a different epoch; do not merge instances.
- **PATH_REUSED:** same pathname now belongs to a distinct recorded object.
- **SAME_CONTENT_ONLY:** distinct identity and path but equal synthetic content digest.
- **NO_DIRECT_LINK:** none of those signals.

A separate check reports coarse timestamp order. This is not clock-skew-adjusted and must not imply a causal chain.

## Reproduce
~~~bash
python3 labs/19-file-identity-reuse-and-event-correlation/lab.py
python3 test_all.py
~~~

## Important Windows details
The `epoch` field is **not** a guaranteed NTFS or Win32 API field. Actual investigation requires volume identity, the appropriate NTFS file reference and sequence information where available, USN Journal evidence, path/copy/rename context and collection provenance. Numeric identifiers can be reused and file-system semantics vary. Neither equal hashes nor matching paths prove who caused an event.

## Questions
1. Why must a file reference be scoped to the volume?
2. How can an old path now point to an unrelated file?
3. What would distinguish a rename from a content-identical copy?
4. Why does the invented epoch not directly transfer to Windows data sources?
5. What additional traces could corroborate a process/file attribution?

## Scope
No filesystem operations, Win32 calls, Registry changes or actual forensic data; this is a safe synthetic correlation exercise.
