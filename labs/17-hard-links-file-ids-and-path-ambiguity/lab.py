"""Synthetic Windows-style hard-link and file identity model; no disk I/O."""
from dataclasses import dataclass, field

@dataclass
class FileObject:
    file_id: int
    links: set[str] = field(default_factory=set)
    handles: set[int] = field(default_factory=set)

class Model:
    def __init__(self):
        self.files: dict[int, FileObject] = {}
        self.paths: dict[str, int] = {}
        self.next_handle = 1

    def create(self, file_id: int, path: str) -> None:
        assert file_id not in self.files and path not in self.paths
        self.files[file_id] = FileObject(file_id, {path})
        self.paths[path] = file_id

    def link(self, existing: str, alias: str) -> bool:
        if existing not in self.paths or alias in self.paths:
            return False
        file_id = self.paths[existing]
        self.paths[alias] = file_id
        self.files[file_id].links.add(alias)
        return True

    def open(self, path: str) -> int | None:
        if path not in self.paths:
            return None
        handle = self.next_handle
        self.next_handle += 1
        self.files[self.paths[path]].handles.add(handle)
        return handle

    def unlink(self, path: str) -> bool:
        if path not in self.paths:
            return False
        obj = self.files[self.paths.pop(path)]
        obj.links.remove(path)
        return True

    def close(self, handle: int) -> None:
        for obj in self.files.values():
            if handle in obj.handles:
                obj.handles.remove(handle)
                return
        raise ValueError("unknown handle")

    def exists(self, file_id: int) -> bool:
        obj = self.files[file_id]
        return bool(obj.links or obj.handles)

def main():
    m = Model()
    m.create(100, "C:/Lab/first.txt")
    assert m.link("C:/Lab/first.txt", "C:/Lab/second.txt")
    assert m.paths["C:/Lab/first.txt"] == m.paths["C:/Lab/second.txt"] == 100
    handle = m.open("C:/Lab/first.txt")
    assert handle is not None
    assert m.unlink("C:/Lab/first.txt")
    assert "C:/Lab/first.txt" not in m.paths
    assert m.exists(100)
    assert m.open("C:/Lab/first.txt") is None
    assert m.unlink("C:/Lab/second.txt")
    assert m.exists(100)  # Open handle still references the object.
    m.close(handle)
    assert not m.exists(100)
    m.create(101, "C:/Lab/first.txt")  # Old path points at a new object.
    assert m.paths["C:/Lab/first.txt"] == 101
    print("11/11 synthetic identity and link checks passed")
    print("No files or Windows APIs were accessed")

if __name__ == "__main__":
    main()
