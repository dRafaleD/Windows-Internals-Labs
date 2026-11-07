"""Offline Registry-like data. Does not read or modify the real Registry."""
registry = {
    r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run": {
        "TrainingUpdater": r"C:\Program Files\TrainingApp\updater.exe",
        "TrainingUnknown": r"C:\Temp\unknown.exe",
    },
    r"HKLM\Software\TrainingApp": {"Version":"1.0"},
}
entries = registry[r"HKCU\Software\Microsoft\Windows\CurrentVersion\Run"]
review = [name for name, path in entries.items() if path.casefold().startswith("c:\\temp\\")]
assert review == ["TrainingUnknown"]
print("Startup entries for contextual review:", review)
print("A suspicious path alone does not prove persistence or malware.")
