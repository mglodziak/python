from sys import stdin
from math import factorial

def dwumian(n, k):
    return factorial(n) // (factorial(k) * factorial(n - k))


def dwm_iter(n, k):
    res=1
    for i in range (1, k+1):
        res = res*(n-i +1)//i
    return res
        
