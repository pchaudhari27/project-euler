def fast_mod_exp_old(x, k, m):
    '''
    Sort fast modular exponentiation of x**k mod m
    Uses that (ab) mod m = [(a mod m)(b mod m)] mod m
    Simpler algorithm using base 10
    '''

    res, exp = 1, 0
    for _ in range(k):
        exp += 1
        res *= x
        res %= m

    return res % m

# use the pow function, but this is good for hand written stuff
def fast_mod_exp(x, k, m):
    '''
    Fast modular exponentiation of x**k mod m
    Uses that (ab) mod m = [(a mod m)(b mod m)] mod m
    Also uses exponent as bits instead of as base 10, "Right-to-Left Binary"
    '''

    res, x = 1, x % m
    while k > 0:
        if k % 2 == 1:
            res *= x
            res %= m
        
        k >>= 1
        x *= x
        x %= m

    return res % m


def exponentation_by_squaring(x, k, recursive = False):
    # recursive
    if recursive:
        if k == 0:
            return 1

        if k < 0:
            return exponentation_by_squaring(1/x, -1*k, recursive)

        # if even exponent
        if k % 2 == 0:
            # x**n = (x**2)**n/2
            return exponentation_by_squaring(x*x, k//2, recursive)
        
        # if odd exponent
        # x**n = x * x**(n-1) = x * (x**2)**(n-1)/2
        return x*exponentation_by_squaring(x*x, (k-1)//2, recursive)

    # iterative
    if k < 0:
        x = 1/x
        k = -1*k
    
    if k == 0:
        return 1
    
    res = 1
    while k > 1:
        # if odd, multiply by an extra x
        if k % 2 == 1:
            res *= x
            k -= 1
        
        x *= x
        k //= 2
    
    return x*res