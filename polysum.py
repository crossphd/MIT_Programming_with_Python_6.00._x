from math import *

from math import *

def polysum(n,s):
    num = .25 * n * s**2
    den = tan(pi/n)
    a = num/den
    p = (n * s)**2
    ans = a+p
    return float("{0:.4f}".format(ans))