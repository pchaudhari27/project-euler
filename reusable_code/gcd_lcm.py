def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    if a == 0 and b == 0:
        return 0
    return abs(a)*abs(b) // gcd(a, b)

def extended_euclidean(a, b):
    s1, s2, r1, r2 = 1, 0, a, b

    while r2 != 0:
        q = r1 // r2
        s1, s2, r1, r2 = s2, s1 - q*s2, r2, r1 - q*r2
    
    if b != 0:
        ret = (r1 - s1*a) // b
    else:
        ret = 0

    return (s1, ret, r1)