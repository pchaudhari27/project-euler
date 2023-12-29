import numpy as np

# quick cache version, using iterative approach
fib_cache = [0] * 10**5
fib_cache[0] = 1
fib_cache[1] = 1
def fib(n):
    if n < 1:
        raise ValueError('why are you plugging in an invalid sequence number') 

    if fib_cache[n] == 0:
        start = fib_cache.index(0)
        for i in range(start, n):
            fib_cache[i] = fib_cache[i-1] + fib_cache[i-2]
    return fib_cache[n-1]

# quick cache version, using recursive approach
def fib(n):
    if n < 1:
        raise ValueError('why are you plugging in an invalid sequence number') 

    if fib_cache[n-1] == 0:
        fib_cache[n-1] = fib(n-1) + fib(n-2)
    return fib_cache[n-1]

# matrix version, very fast (can't use numpy because of floating point arithmetic)
def fib(n):
    v1, v2, v3 = 1, 1, 0    # initialise a matrix [[1,1],[1,0]]
    for rec in bin(n)[3:]:  # perform fast exponentiation of the matrix (quickly raise it to the nth power)
        calc = v2*v2
        v1, v2, v3 = v1*v1+calc, (v1+v3)*v2, calc+v3*v3
        if rec=='1':
            v1, v2, v3 = v1+v2, v1, v2
    return v2
