"""Offline FILETIME arithmetic with invented values; no Windows API."""
from datetime import datetime,timedelta,timezone

BASE=datetime(1601,1,1,tzinfo=timezone.utc)
UNIX_OFFSET=116444736000000000
MAX_TICKS=(1<<64)-1

def decode(ticks):
    if type(ticks) is not int or not 0<=ticks<=MAX_TICKS:
        return "INVALID_TICKS",None,None
    micros,remainder=divmod(ticks,10)
    try:
        dt=BASE+timedelta(microseconds=micros)
    except OverflowError:
        return "OUT_OF_RANGE",None,None
    return "OK",dt.isoformat(),remainder

def encode(value):
    dt=datetime.fromisoformat(value)
    if dt.tzinfo is None:
        raise ValueError("explicit timezone required")
    delta=dt.astimezone(timezone.utc)-BASE
    result=((delta.days*86400+delta.seconds)*1000000+delta.microseconds)*10
    if not 0<=result<=MAX_TICKS:
        raise ValueError("out of FILETIME range")
    return result

def main():
    cases=[
        (0,"OK","1601-01-01T00:00:00+00:00",0),
        (1,"OK","1601-01-01T00:00:00+00:00",1),
        (9,"OK","1601-01-01T00:00:00+00:00",9),
        (10,"OK","1601-01-01T00:00:00.000001+00:00",0),
        (UNIX_OFFSET,"OK","1970-01-01T00:00:00+00:00",0),
        (UNIX_OFFSET+10000000,"OK","1970-01-01T00:00:01+00:00",0),
        (UNIX_OFFSET-10000000,"OK","1969-12-31T23:59:59+00:00",0),
        (UNIX_OFFSET+17,"OK","1970-01-01T00:00:00.000001+00:00",7),
        (-1,"INVALID_TICKS",None,None),
        (True,"INVALID_TICKS",None,None),
        ("42","INVALID_TICKS",None,None),
        (MAX_TICKS,"OUT_OF_RANGE",None,None),
        (MAX_TICKS+1,"INVALID_TICKS",None,None),
    ]
    for ticks,*expected in cases:
        result=decode(ticks)
        assert result==tuple(expected),(ticks,result)
        print(f"{str(ticks):>22} {result}")
    assert encode("1970-01-01T00:00:00+00:00")==UNIX_OFFSET
    assert encode("1970-01-01T03:00:00+03:00")==UNIX_OFFSET
    assert encode("1970-01-01T00:00:01+00:00")==UNIX_OFFSET+10000000
    for bad in ("1970-01-01T00:00:00","1600-01-01T00:00:00+00:00"):
        try:
            encode(bad)
        except ValueError:
            pass
        else:
            raise AssertionError("Expected rejected timestamp")
    print("13 decode cases + 5 encode checks passed")

if __name__=="__main__":
    main()
