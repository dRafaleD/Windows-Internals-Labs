"""Synthetic Windows event records, not real event log collection."""
from collections import Counter

events = [
    {"provider":"Microsoft-Windows-Security-Auditing","event_id":4624,"channel":"Security","actor":"demo"},
    {"provider":"TrainingProvider","event_id":4624,"channel":"Application","actor":"demo"},
    {"provider":"Microsoft-Windows-Security-Auditing","event_id":4688,"channel":"Security","actor":"demo"},
]
counts = Counter((e["provider"], e["event_id"]) for e in events)
assert len(counts) == 3
assert counts[("Microsoft-Windows-Security-Auditing",4624)] == 1
print("Distinct provider/event combinations:", dict(counts))
