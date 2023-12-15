def gcd(a,b):
    if a == 0:
        return b
    return gcd(b % a, a)

def lcm(a,b):
    if a == 0 and b == 0:
        return 0
    return abs(a)*abs(b) // gcd(a, b)