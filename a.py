from math import gcd
from functools import reduce

def lcm(a, b):
    return a * b // gcd(a, b)

def lcm_multiple(numbers):
    return reduce(lcm, numbers)

int(input())
print(lcm_multiple(list(map(int,input().split()))))
