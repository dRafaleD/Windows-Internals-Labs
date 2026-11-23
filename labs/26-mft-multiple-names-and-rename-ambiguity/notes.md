# Day 26 — MFT Multiple Names and Rename Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python](lab.py)

## After Day 25
The previous lab checked whether a fictional USN old/new-name pair matched **MFT snapshots** of the same file reference. Day 26 adds another issue: an NTFS file may have **multiple names**, including through hard links or multiple file-name records. Observing two names does not necessarily identify a single rename operation.

## Model
The fictional MFT snapshot stores an array of observed names rather than just one. A proposed rename still requires matching volume, file index and sequence, increasing USN order, absence of known acquisition gaps, and compatible before/after snapshot times.

- `CONSISTENT_CANDIDATE`: simple single-name observation fits the proposed change.
- `OLD_NAME_STILL_PRESENT`: the old name remains visible in the later snapshot.
- `MULTI_NAME_CONTEXT`: one or both snapshots have more names than the basic rename model accounts for.
- Other labels mark missing evidence, file-reference reuse and contradictions.

## Run
```bash
python3 labs/26-mft-multiple-names-and-rename-ambiguity/lab.py
python3 test_all.py
```

## Questions
Why can one file have multiple names? Why should a remaining old name prevent a simple one-to-one rename conclusion? Why does a snapshot show observed state rather than a complete history? How can sequence-number reuse confuse identity?

## Limits
Toy flags and records, not a genuine $MFT or $UsnJrnl parser. Real Windows file-name attributes, directories, references and hard-link semantics require source-specific validation. No real Windows resources are accessed.
