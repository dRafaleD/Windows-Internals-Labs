# Day 18 — File-ID Reuse, Generations and Handle Evidence

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## From Day 17
Hard links allow several paths to name one file object. After all names and open handles are gone, a filesystem may eventually **reuse a numeric file identifier** for a new object. Therefore, seeing the same file ID at different times is not always sufficient to establish continuous identity.

## Toy model
A fictional file with ID 42 starts at `a.txt`, gains a hard link `b.txt`, then has both names removed. An open handle keeps the toy object alive, so reuse of ID 42 is rejected until that handle is closed. After closure, a new object can use ID 42 but receives a different **epoch**.

This epoch is **invented for the demonstration**; do not mistake it for a guaranteed Windows/NTFS field. Real analysis should correlate volume context, record sequence information where available, timestamps, USN events, paths and content fingerprints. File systems and APIs vary.

## Reproduce
~~~bash
python3 labs/18-file-id-reuse-generations-and-handle-evidence/lab.py
python3 test_all.py
~~~

## Questions
1. Why may two paths share one file ID at a given time?
2. When could the same numeric ID denote a *different* file object?
3. Why is an old event's path insufficient to prove what a process opened later?
4. How does an open handle affect lifetime in this teaching abstraction?
5. Which actual NTFS artifacts would you examine before asserting identity continuity?

## Limitations
No real file operations, Windows APIs or NTFS parser. The simplified collection and reuse rules are not exact Windows kernel semantics.
