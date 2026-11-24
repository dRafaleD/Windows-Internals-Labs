# Day 27 — MFT Parent References and Path Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Code](lab.py)

Day 26 represented multiple names for a fictional file. Day 27 distinguishes a name in one parent directory from an identical name in another. Each observed name contains a parent index, parent sequence and text. Same-parent name change and cross-parent move are only **candidates**. A changed parent sequence, multiple links, missing names or different file identity prevents a straightforward conclusion.

**Questions:** Why is filename text alone insufficient to identify a directory entry? How can a reused parent reference mislead a reconstruction? Why do snapshots not establish an exact event history?

All references are invented. This is not an NTFS parser and does not reconstruct absolute paths, timestamps, or real rename events. No Windows access.

## Run
```bash
python3 labs/27-mft-parent-references-and-path-ambiguity/lab.py
python3 test_all.py
```
