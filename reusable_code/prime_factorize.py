from sieve_of_eratosthenes import sieve

def prime_factorize(num, primes = None):
    prime_factors = []
    if not primes:
        _, primes = sieve(num)
    
    n = num
    for p in primes:
        while n % p == 0:
            prime_factors.append(p)
            n //= p

    return prime_factors