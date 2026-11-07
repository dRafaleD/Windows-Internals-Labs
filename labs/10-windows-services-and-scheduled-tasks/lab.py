"""Compare synthetic scheduled-task metadata. Nothing is scheduled or executed."""
baseline = {"TrainingBackup": {"path":r"C:\Program Files\TrainingApp\backup.exe"}}
current = {
    "TrainingBackup": {"path":r"C:\Program Files\TrainingApp\backup.exe"},
    "TrainingNewTask": {"path":r"C:\Temp\helper.exe"},
}
added = sorted(set(current) - set(baseline))
assert added == ["TrainingNewTask"]
print("New configurations to review:", added)
print("This is not evidence that the task executed.")
