"""Offline event correlation; no ETW subscriptions or Sysmon installation."""
creation = [
 {"guid":"proc-a","pid":200,"image":"training.exe","time":"2026-06-01T12:00:00Z"},
 {"guid":"proc-b","pid":201,"image":"training.exe","time":"2026-06-01T12:02:00Z"},
]
network = [
 {"guid":"proc-b","destination":"192.0.2.8","time":"2026-06-01T12:03:00Z"},
]
indexed = {e["guid"]: e for e in creation}
joined = [(indexed[e["guid"]],e) for e in network if e["guid"] in indexed]
assert len(joined) == 1
assert joined[0][0]["pid"] == 201
print("Correlated process:", joined[0][0]["guid"], joined[0][0]["pid"])
print("Duplicate image names alone cannot distinguish these processes.")
