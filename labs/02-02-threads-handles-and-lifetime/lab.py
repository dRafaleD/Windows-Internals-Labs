"""Offline table of handle scopes, not a Windows kernel handle enumerator."""
handles = {
    (100, 40): {"type":"File", "object":"training-a.txt"},
    (200, 40): {"type":"Event", "object":"training-ready"},
    (100, 41): {"type":"Event", "object":"training-signal"},
}
assert handles[(100,40)]["object"] != handles[(200,40)]["object"]
print("pid=100 handle=40 ->", handles[(100,40)])
print("pid=200 handle=40 ->", handles[(200,40)])
old = handles.pop((100,41))
handles[(100,41)] = {"type":"File","object":"training-b.txt"}
assert old != handles[(100,41)]
print("Handle values may be reused after close.")
