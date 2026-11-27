"""Reconstruct unsigned fictional FILETIME values from two 32-bit words."""
MASK=(1<<32)-1
MAX=(1<<64)-1
UNIX=116444736000000000

def combine(low,high):
    if any(type(x) is not int or not 0<=x<=MASK for x in (low,high)):
        raise ValueError("invalid unsigned word")
    return (high<<32)|low

def split(ticks):
    if type(ticks) is not int or not 0<=ticks<=MAX:
        raise ValueError("invalid tick value")
    return ticks&MASK,ticks>>32

def main():
    for ticks in (0,1,MASK,MASK+1,UNIX,UNIX+17,MAX):
        low,high=split(ticks)
        assert combine(low,high)==ticks
        assert low.to_bytes(4,"little")+high.to_bytes(4,"little")==ticks.to_bytes(8,"little")
        print(f"{ticks:20} low={low:08x} high={high:08x}")
    for low,high in ((-1,0),(0,MASK+1),(True,0),(0,"1")):
        try:
            combine(low,high)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid word accepted")
    for ticks in (-1,MAX+1,False):
        try:
            split(ticks)
        except ValueError:
            pass
        else:
            raise AssertionError("invalid ticks accepted")
    print("14/14 word reconstruction cases passed")

if __name__=="__main__":
    main()
