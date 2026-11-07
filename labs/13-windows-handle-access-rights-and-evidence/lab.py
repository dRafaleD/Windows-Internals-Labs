"""Toy Windows file-handle rights interpretation; no Win32 API calls."""
READ_DATA=0x0001
WRITE_DATA=0x0002
rights={
 "training-reader":READ_DATA,
 "training-editor":READ_DATA | WRITE_DATA,
 "training-none":0,
}
def decode(mask):
    return {"read":bool(mask & READ_DATA),"write":bool(mask & WRITE_DATA)}
assert decode(rights["training-reader"])=={"read":True,"write":False}
assert decode(rights["training-editor"])=={"read":True,"write":True}
assert decode(rights["training-none"])=={"read":False,"write":False}
for process,mask in rights.items():
    print(process, decode(mask))
print("Illustrative mask only: not a complete Windows access check.")
