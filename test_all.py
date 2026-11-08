"""Offline lab smoke runner; each subprocess gets an isolated working directory."""
from pathlib import Path
import subprocess
import sys

ROOT = Path(__file__).resolve().parent
paths = sorted((ROOT / "labs").glob("*/lab.py"))
if len(paths) != 14:
    raise SystemExit(f"Expected 14 lab.py scripts, found {len(paths)}")
errors = []
for path in paths:
    try:
        result = subprocess.run([sys.executable, str(path)], cwd=path.parent,
                                capture_output=True, text=True, timeout=15, check=False)
        print(("[PASS] " if result.returncode == 0 else "[FAIL] ") + str(path.relative_to(ROOT)))
        if result.returncode:
            errors.append((str(path.relative_to(ROOT)), result.stderr or result.stdout))
    except subprocess.TimeoutExpired:
        errors.append((str(path.relative_to(ROOT)), "timeout"))
for path, error in errors:
    print(path + ": " + error, file=sys.stderr)
if errors:
    raise SystemExit(1)
print("14/14 Windows Internals offline checks passed.")
