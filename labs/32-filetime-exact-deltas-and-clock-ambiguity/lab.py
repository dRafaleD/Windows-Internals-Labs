"""Compare invented FILETIME ticks without floating-point rounding."""
from fractions import Fraction
MAX=(1<<64)-1
UNIX=116444736000000000

def compare(a,b,uncertainty_a=0,uncertainty_b=0):
    if any(type(x) is not int for x in (a,b,uncertainty_a,uncertainty_b)):
        return "INVALID",None
    if not (0<=a<=MAX and 0<=b<=MAX) or min(uncertainty_a,uncertainty_b)<0:
        return "INVALID",None
    delta=Fraction(b-a,10000000)
    if a+uncertainty_a<b-uncertainty_b:
        return "A_BEFORE_B",delta
    if b+uncertainty_b<a-uncertainty_a:
        return "B_BEFORE_A",delta
    return "ORDER_UNCERTAIN",delta

def main():
    cases=[
        (UNIX,UNIX+1,0,0,("A_BEFORE_B",Fraction(1,10000000))),
        (UNIX+1,UNIX,0,0,("B_BEFORE_A",Fraction(-1,10000000))),
        (UNIX,UNIX,0,0,("ORDER_UNCERTAIN",Fraction(0))),
        (UNIX,UNIX+10,5,5,("ORDER_UNCERTAIN",Fraction(1,1000000))),
        (UNIX,UNIX+11,5,5,("A_BEFORE_B",Fraction(11,10000000))),
        (UNIX,UNIX+10000000,0,0,("A_BEFORE_B",Fraction(1))),
        (0,MAX,0,0,("A_BEFORE_B",Fraction(MAX,10000000))),
        (-1,UNIX,0,0,("INVALID",None)),
        (UNIX,MAX+1,0,0,("INVALID",None)),
        (UNIX,UNIX,-1,0,("INVALID",None)),
        (True,UNIX,0,0,("INVALID",None)),
    ]
    for *args,want in cases:
        got=compare(*args)
        assert got==want,(args,got)
        print(got)
    print("11/11 exact delta cases passed")

if __name__=="__main__":
    main()
