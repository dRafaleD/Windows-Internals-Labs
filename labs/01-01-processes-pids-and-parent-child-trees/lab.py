"""Synthetic PID/PPID tree. Does not inspect or alter real processes."""
processes = [
    {"pid":4, "ppid":0, "name":"System"},
    {"pid":100, "ppid":4, "name":"training-shell"},
    {"pid":120, "ppid":100, "name":"training-helper"},
    {"pid":130, "ppid":999, "name":"training-orphan"},
]
by_pid = {p["pid"]: p for p in processes}
assert len(by_pid) == len(processes)
for p in processes:
    parent = by_pid.get(p["ppid"])
    print(f'{p["pid"]:>5} {p["name"]} <- {parent["name"] if parent else "not captured"}')
assert by_pid[130]["ppid"] not in by_pid
print("Missing parent is not, by itself, evidence of maliciousness.")
