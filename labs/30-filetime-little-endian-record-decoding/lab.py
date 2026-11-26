"""Decode invented eight-byte FILETIME fields without touching Windows."""
from datetime import datetime,timedelta,timezone

BASE=datetime(1601,1,1,tzinfo=timezone.utc)
UNIX=116444736000000000

def decode(raw,zero_is_missing=False):
    if not isinstance(raw,bytes) or len(raw)!=8:
        return "INVALID_FIELD",None
    ticks=int.from_bytes(raw,"little",signed=False)
    if ticks==0 and zero_is_missing:
        return "MISSING_BY_CONTRACT",None
    micros,rem=divmod(ticks,10)
    try:
        date=BASE+timedelta(microseconds=micros)
    except OverflowError:
        return "OUT_OF_RANGE",None
    return "OK",(date.isoformat(),rem,ticks)

def field(n):
    return n.to_bytes(8,"little")

def main():
    cases=[
        (field(0),False,"OK"),
        (field(0),True,"MISSING_BY_CONTRACT"),
        (field(1),False,"OK"),
        (field(UNIX),False,"OK"),
        (field(UNIX+17),False,"OK"),
        (field((1<<64)-1),False,"OUT_OF_RANGE"),
        (b"\x00"*7,False,"INVALID_FIELD"),
        (b"\x00"*9,False,"INVALID_FIELD"),
        ("not bytes",False,"INVALID_FIELD"),
    ]
    for raw,missing,want in cases:
        got,value=decode(raw,missing)
        assert got==want,(got,want)
        if value:
            assert field(value[2])==raw
        print(got,value)
    assert field(UNIX).hex()=="00803ed5deb19d01"
    assert decode(field(UNIX))[1][0]=="1970-01-01T00:00:00+00:00"
    assert decode(field(UNIX+17))[1][1]==7
    print("9 field cases + 3 decoding checks passed")

if __name__=="__main__":
    main()
