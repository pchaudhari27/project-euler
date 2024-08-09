from sieve_of_eratosthenes import sieve
from miller_rabin import miller_rabin

from collections import Counter
from itertools import product

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

# factorization with caching for repeated calls
factor_cache = {1: [1]}
def factorize(num):
    if miller_rabin(num):
        factor_cache[num] = [1,num]
        return factor_cache[num]
    
    if num not in factor_cache:
        if num < 10**5:
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

            factor_cache[num] =  left_factors + right_factors
        else:
            factors = set()
            i = 2
            while i*i <= num:
                if num % i == 0 and num // i < 10**5:
                    break
                i += 1
            
            smalls = factorize(i)
            bigs = factorize(num // i)

            for s,b in product(smalls, bigs):
                factors.add(s*b)

            factor_cache[num] = sorted(factors)
    
    return factor_cache[num]