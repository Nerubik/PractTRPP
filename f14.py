import math
n=11
def f14(n):
    if n==0:
        return 5
    elif n>0:
        return math.cos(f14(n-1))-math.sin(f14(n-1))
f14(n)

