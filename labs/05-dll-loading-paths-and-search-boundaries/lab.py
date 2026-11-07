"""Offline trusted-path policy; does not load any DLL."""
from pathlib import PureWindowsPath

TRUSTED_ROOT = PureWindowsPath(r"C:\Program Files\TrainingApp\lib")
def trusted_library(path_text):
    path = PureWindowsPath(path_text)
    parts = [x.casefold() for x in path.parts]
    root = [x.casefold() for x in TRUSTED_ROOT.parts]
    return path.is_absolute() and parts[:len(root)] == root and path.suffix.casefold() == ".dll"
assert trusted_library(r"C:\Program Files\TrainingApp\lib\example.dll")
assert not trusted_library("example.dll")
assert not trusted_library(r"C:\Users\Public\example.dll")
print("Synthetic path policy checks passed.")
print("This is not an implementation of Windows loader search order.")
