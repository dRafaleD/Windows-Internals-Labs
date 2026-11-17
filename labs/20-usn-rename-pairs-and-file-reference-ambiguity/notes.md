# Day 20 — USN Rename Pairs and File Reference Ambiguity

[English](notes.md) · [Türkçe](notes.tr.md) · [Offline Python practice](lab.py)

## Connection to Day 19
Day 19 distinguished reused numeric file IDs from continuous logical file identity. Day 20 applies that caution to a **fictional NTFS USN Journal rename sequence**.

## Model
Two synthetic records may form a rename candidate when:
- the first reason is `RENAME_OLD_NAME`, and the later record says `RENAME_NEW_NAME`;
- their volume, numeric file ID and **invented toy epoch** match;
- their USN order increases within a small illustrative record-gap window.

The demo checks an ordinary candidate and eight negative examples: changed file ID or volume, different toy epoch, reversed/equal USN, large gap and unexpected reason flags.

## Critical caveats
- Real NTFS USN records carry **reason bit flags**, not necessarily a single exclusive string; a real parser needs correct layout, version, range, encoding and flag handling.
- The `toy_epoch` is **not an actual guaranteed NTFS field**. Real file-reference sequence information, journal continuity and reuse require their own interpretation.
- USN ordering and adjacent events can be affected by missed journal records and collection gaps. A matched pair supports a *rename hypothesis*; it does not establish a user, process, causal chain or complete history.

## Reproduce
~~~bash
python3 labs/20-usn-rename-pairs-and-file-reference-ambiguity/lab.py
python3 test_all.py
~~~

## Questions
1. Why do old-name and new-name events need a common file identity?
2. What risks arise if numeric file IDs are reused?
3. Why should a real parser handle bitwise USN reason flags?
4. What if journal wraparound removed one event?
5. What process telemetry would help investigate who initiated the rename?

## Safety
No Windows APIs, files, NTFS volumes or USN journal are accessed; these are invented records for learning.
