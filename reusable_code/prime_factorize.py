from sieve_of_eratosthenes import sieve
from collections import Counter

def prime_factorize(num, prime_bins = None, primes = None):
    prime_factors = []
    if not primes:
        prime_bins, primes = sieve(num)
    
    if prime_bins[n]:
        return Counter([n])

    n = num
    for p in primes:
        if n == 1 or p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p

    return Counter(prime_factors)