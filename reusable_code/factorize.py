from sieve_of_eratosthenes import sieve
from collections import Counter

def prime_factorize(num, prime_bins = None, primes = None):
    prime_factors = []
    if not primes:
        prime_bins, primes = sieve(num)
    
    if prime_bins[num]:
        return Counter([num])

    n = num
    for p in primes:
        if n == 1 or p > n:
            break
        while n % p == 0:
            prime_factors.append(p)
            n //= p

    return Counter(prime_factors)

def factorize(num, prime_bins = None):
    if not prime_bins:
        prime_bins, _ = sieve(num)

    if prime_bins[num]:
        return [1,num]
    
    left_factors = [1]
    right_factors = [num]
    i = 2

    while i*i < num:
        if num % i == 0:
            left_factors.append(i)
            right_factors = [num // i] + right_factors

        i += 1

    if i*i == num:
        left_factors.append(i)

    return left_factors + right_factors