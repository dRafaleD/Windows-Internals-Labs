"""Synthetic Windows event correlation. No actual evidence or live system access."""
from datetime import datetime, timezone

records = [
 {"source":"synthetic-file","id":"f1","time":"2026-06-05T12:01:00Z","guid":"proc-a","kind":"file_create","path":"training.txt"},
 {"source":"synthetic-process","id":"p1","time":"2026-06-05T12:00:00Z","guid":"proc-a","kind":"process_create","path":"training.exe"},
 {"source":"synthetic-audit","id":"a1","time":"2026-06-05T11:59:00Z","guid":None,"kind":"login","path":None},
]
def time(record):
    return datetime.fromisoformat(record["time"].replace("Z","+00:00")).astimezone(timezone.utc)
timeline = sorted(records, key=lambda r:(time(r),r["id"]))
process_guids = {r["guid"] for r in records if r["kind"] == "process_create"}
file_events = [r for r in records if r["kind"] == "file_create"]
assert len(file_events) == 1 and file_events[0]["guid"] in process_guids
for r in timeline: print(r["time"], r["source"], r["id"], r["kind"])
report = {"correlation":"file event references observed process GUID",
          "actor_attribution":"inconclusive",
          "missing":["direct initiating-user context","independent file-content evidence"]}
assert report["actor_attribution"] == "inconclusive"
print("Report:", report)
