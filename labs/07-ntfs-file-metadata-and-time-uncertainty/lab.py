"""Synthetic/temporary file metadata only. Never touches evidence files."""
import tempfile
from pathlib import Path
from datetime import datetime, timezone

with tempfile.TemporaryDirectory(prefix="win-internals-") as td:
    path = Path(td) / "training.txt"
    path.write_text("version one", encoding="utf-8")
    first = path.stat()
    path.write_text("version two (changed)", encoding="utf-8")
    second = path.stat()
    assert second.st_size != first.st_size
    print("size:", first.st_size, "->", second.st_size)
    print("mtime UTC:", datetime.fromtimestamp(second.st_mtime, timezone.utc).isoformat())
print("Temporary data removed. This does not parse the NTFS MFT or USN journal.")
