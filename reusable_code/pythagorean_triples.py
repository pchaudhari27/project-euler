from gcd_lcm import gcd

# Euclid's formula
def euclid_pythagorean(max_perimeter):
    triples = set()
    to_check = [(1,2)]
    seen = set()
    while to_check:
        m,n = to_check.pop(0)
        if (m,n) in seen: continue

        seen.add((m,n))
        a,b,c = m*m - n*n, 2*m*n, m*m + n*n

        # require gcd = 1 for primitive triples
        if m > n and gcd(m,n) == 1 and (m + n) % 2 == 1 and a + b + c <= max_perimeter:
            triples.add((a,b,c))
            if n + 1 < m:
                to_check.append((n+1, m))
            to_check.append((n, m+1))

    return triples

# parent child relationships from Berggren
def berggren_pythagorean(max_perimeter):
    triples = set()
    triples_to_check = [(3,4,5)]

    while triples_to_check:
        # pop side lengths of previously calculated primitive
        a,b,c = triples_to_check.pop(0)
        triples.add((a,b,c))

        # transformation 1
        new_a, new_b, new_c = a - 2*b + 2*c, 2*a - b + 2*c, 2*a - 2*b + 3*c
        if new_a + new_b + new_c <= max_perimeter:
            triples_to_check.append((min(new_a, new_b), max(new_a, new_b), new_c))
        
        # transformation 2
        new_a, new_b, new_c = a + 2*b + 2*c, 2*a + b + 2*c, 2*a + 2*b + 3*c
        if new_a + new_b + new_c <= max_perimeter:
            triples_to_check.append((min(new_a, new_b), max(new_a, new_b), new_c))

        # transformation 3
        new_a, new_b, new_c = -1*a + 2*b + 2*c, -2*a + b + 2*c, -2*a + 2*b + 3*c
        if new_a + new_b + new_c <= max_perimeter:
            triples_to_check.append((min(new_a, new_b), max(new_a, new_b), new_c))

    return triples