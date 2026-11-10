"""Synthetic Windows file delete-pending lifecycle; NO real filesystem operations."""
from dataclasses import dataclass, field

READ = 0b001
WRITE = 0b010
DELETE = 0b100

@dataclass(frozen=True)
class Handle:
    desired_access: int
    share_mode: int

@dataclass
class FileModel:
    handles: dict[int, Handle] = field(default_factory=dict)
    next_handle_id: int = 1
    delete_pending: bool = False
    deleted: bool = False

    def open(self, incoming: Handle) -> int | None:
        if self.delete_pending or self.deleted:
            return None
        for existing in self.handles.values():
            if incoming.desired_access & ~existing.share_mode:
                return None
            if existing.desired_access & ~incoming.share_mode:
                return None
        handle_id = self.next_handle_id
        self.next_handle_id += 1
        self.handles[handle_id] = incoming
        return handle_id

    def request_delete(self, caller_authorized: bool) -> bool:
        if self.deleted or self.delete_pending or not caller_authorized:
            return False
        if any(not (h.share_mode & DELETE) for h in self.handles.values()):
            return False
        self.delete_pending = True
        if not self.handles:
            self.deleted = True
        return True

    def close(self, handle_id: int) -> None:
        if handle_id not in self.handles:
            raise ValueError("unknown or already closed handle")
        del self.handles[handle_id]
        if self.delete_pending and not self.handles:
            self.deleted = True


def main() -> None:
    blocking = FileModel()
    reader = blocking.open(Handle(READ, READ))
    assert reader is not None
    assert blocking.request_delete(caller_authorized=True) is False
    assert not blocking.delete_pending
    blocking.close(reader)
    print("01: handle omitting SHARE_DELETE blocks request")

    model = FileModel()
    first = model.open(Handle(READ, READ | DELETE))
    second = model.open(Handle(READ, READ | DELETE))
    assert first is not None and second is not None
    assert model.request_delete(caller_authorized=False) is False
    assert model.request_delete(caller_authorized=True) is True
    assert model.delete_pending and not model.deleted
    assert model.open(Handle(READ, READ | DELETE)) is None
    model.close(first)
    assert not model.deleted
    model.close(second)
    assert model.deleted
    assert model.open(Handle(READ, READ | DELETE)) is None
    print("02: SHARE_DELETE does not grant authorization")
    print("03: pending state rejects new opens in this simplified model")
    print("04: final handle close completes modeled deletion")
    print("4/4 synthetic checks passed; no Windows API or file was touched.")

if __name__ == "__main__":
    main()
