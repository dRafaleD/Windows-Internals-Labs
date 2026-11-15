"""Synthetic file-ID reuse after unlink and handle closure; no filesystem I/O."""
from dataclasses import dataclass, field

@dataclass
class Object:
    file_id: int
    epoch: int  # Toy-model identity marker, not an NTFS generation field.
    paths: set[str] = field(default_factory=set)
    handles: set[int] = field(default_factory=set)

class Model:
    def __init__(self):
        self.objects: dict[int, Object] = {}
        self.paths: dict[str, int] = {}
        self.next_epoch = 1
        self.next_handle = 1

    def create(self, file_id: int, path: str) -> Object | None:
        if file_id in self.objects or path in self.paths:
            return None
        obj = Object(file_id, self.next_epoch, {path})
        self.next_epoch += 1
        self.objects[file_id] = obj
        self.paths[path] = file_id
        return obj

    def link(self, old: str, new: str) -> bool:
        if old not in self.paths or new in self.paths:
            return False
        file_id = self.paths[old]
        self.paths[new] = file_id
        self.objects[file_id].paths.add(new)
        return True

    def open(self, path: str) -> int | None:
        if path not in self.paths:
            return None
        handle = self.next_handle
        self.next_handle += 1
        self.objects[self.paths[path]].handles.add(handle)
        return handle

    def collect(self, file_id: int) -> None:
        obj = self.objects[file_id]
        if not obj.paths and not obj.handles:
            del self.objects[file_id]

    def unlink(self, path: str) -> bool:
        if path not in self.paths:
            return False
        file_id = self.paths.pop(path)
        self.objects[file_id].paths.remove(path)
        self.collect(file_id)
        return True

    def close(self, handle: int) -> bool:
        for file_id, obj in list(self.objects.items()):
            if handle in obj.handles:
                obj.handles.remove(handle)
                self.collect(file_id)
                return True
        return False

def main():
    passed = 0
    def check(value):
        nonlocal passed
        assert value
        passed += 1

    m = Model()
    first = m.create(42, "C:/Lab/a.txt")
    check(first is not None and first.epoch == 1)
    check(m.link("C:/Lab/a.txt", "C:/Lab/b.txt"))
    handle = m.open("C:/Lab/a.txt")
    check(handle is not None)
    check(m.unlink("C:/Lab/a.txt"))
    check(m.unlink("C:/Lab/b.txt"))
    check(42 in m.objects)  # Open handle keeps the toy object alive.
    check(m.create(42, "C:/Lab/new.txt") is None)
    check(m.close(handle))
    check(42 not in m.objects)
    second = m.create(42, "C:/Lab/new.txt")
    check(second is not None and second.epoch != first.epoch)
    check((first.file_id, first.epoch) != (second.file_id, second.epoch))
    print(f"{passed}/{passed} synthetic file-identity checks passed")
    print("The epoch is an invented marker; no real NTFS files were touched.")

if __name__ == "__main__":
    main()
