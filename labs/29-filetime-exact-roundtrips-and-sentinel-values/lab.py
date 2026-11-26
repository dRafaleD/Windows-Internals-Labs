"""Exact arithmetic for fictional FILETIME values, not live Windows records."""
from datetime import datetime,timedelta,timezone

BASE=datetime(1601,1,1,tzinfo=timezone.utc)
OFFSET=116444736000000000
MAX=(1<<64)-1

def decode(ticks,zero_is_missing=False):
    if type(ticks) is not int or not 0<=ticks<=MAX:
        return "INVALID",None,None
    if zero_is_missing and ticks==0:
        return "MISSING",None,None
    micros,remainder=divmod(ticks,10)
    try:
        dt=BASE+timedelta(microseconds=micros)
    except OverflowError:
        return "OUT_OF_RANGE",None,None
    return "OK",dt,remainder

def encode(dt,remainder):
    if dt.tzinfo is None or type(remainder) is not int or not 0<=remainder<10:
        raise ValueError("invalid datetime or remainder")
    delta=dt.astimezone(timezone.utc)-BASE
    ticks=((delta.days*86400+delta.seconds)*1000000+delta.microseconds)*10+remainder
    if not 0<=ticks<=MAX:
        raise ValueError("out of range")
    return ticks

def main():
    for ticks in (0,1,9,10,17,OFFSET-1,OFFSET,OFFSET+7,OFFSET+10000001):
        status,dt,remainder=decode(ticks)
        assert status=="OK" and encode(dt,remainder)==ticks
        print(ticks,dt.isoformat(),remainder)
    assert decode(0,True)==("MISSING",None,None)
    assert decode(-1)==("INVALID",None,None)
    assert decode(True)==("INVALID",None,None)
    assert decode(MAX)==("OUT_OF_RANGE",None,None)
    assert decode(MAX+1)==("INVALID",None,None)
    for dt,remainder in ((BASE,10),(BASE,-1),(BASE,True),(datetime(1970,1,1),0)):
        try:
            encode(dt,remainder)
        except ValueError:
            pass
        else:
            raise AssertionError("bad input accepted")
    print("9 round trips + 9 boundary checks passed")

if __name__=="__main__":
    main()
