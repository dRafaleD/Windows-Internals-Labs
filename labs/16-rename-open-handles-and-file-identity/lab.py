"""Synthetic Windows rename and open-handle identity model; no filesystem I/O."""
from dataclasses import dataclass, field

READ = 0b001
WRITE = 0b010
DELETE = 0b100

@dataclass(frozen=True)
class Handle:
    file_id: int
    desired_access: int
    share_mode: int

@dataclass
class FileRecord:
    file_id: int
    path: str
    handles: dict[int, Handle] = field(default_factory=dict)

@dataclass
class Model:
    files: dict[int, FileRecord] = field(default_factory=dict)
    paths: dict[str, int] = field(default_factory=dict)
    next_handle: int = 1

    def add_file(self, file_id: int, path: str) -> None:
        assert file_id not in self.files and path not in self.paths
        self.files[file_id] = FileRecord(file_id, path)
        self.paths[path] = file_id

    def open(self, path: str, access: int, share: int) -> int | None:
        file_id = self.paths.get(path)
        if file_id is None:
            return None
        record = self.files[file_id]
        for old in record.handles.values():
            if access & ~old.share_mode:
                return None
            if old.desired_access & ~share:
                return None
        hid = self.next_handle
        self.next_handle += 1
        record.handles[hid] = Handle(file_id, access, share)
        return hid

    def close(self, handle_id: int) -> None:
        for record in self.files.values():
            if handle_id in record.handles:
                del record.handles[handle_id]
                return
        raise ValueError("unknown handle")

    def rename(self, old: str, new: str, caller_has_delete_access: bool) -> bool:
        file_id = self.paths.get(old)
        if file_id is None or new in self.paths or old == new:
            return False
        if not caller_has_delete_access:
            return False
        record = self.files[file_id]
        if any(not (h.share_mode & DELETE) for h in record.handles.values()):
            return False
        del self.paths[old]
        self.paths[new] = file_id
        record.path = new
        return True

def main() -> None:
    m = Model()
    m.add_file(101, "C:/Lab/old.txt")
    m.add_file(102, "C:/Lab/existing.txt")
    blocked = m.open("C:/Lab/old.txt", READ, READ)
    assert blocked is not None
    assert m.rename("C:/Lab/old.txt", "C:/Lab/new.txt", True) is False
    m.close(blocked)
    shared = m.open("C:/Lab/old.txt", READ, READ | DELETE)
    assert shared is not None
    assert m.rename("C:/Lab/old.txt", "C:/Lab/new.txt", False) is False
    assert m.rename("C:/Lab/old.txt", "C:/Lab/existing.txt", True) is False
    assert m.rename("C:/Lab/old.txt", "C:/Lab/new.txt", True) is True
    assert m.paths.get("C:/Lab/old.txt") is None
    assert m.files[101].handles[shared].file_id == 101
    assert m.files[101].path == "C:/Lab/new.txt"
    new_handle = m.open("C:/Lab/new.txt", READ, READ | DELETE)
    assert new_handle is not None
    assert m.open("C:/Lab/old.txt", READ, READ | DELETE) is None
    m.close(new_handle)
    m.close(shared)
    print("10/10 synthetic rename and handle assertions passed.")
    print("No Win32 APIs, disk files or Registry keys were changed.")

if __name__ == "__main__":
    main()
