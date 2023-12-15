import math

# find continued fraction coefs
def continued_frac(n, suppress = True):
    root = math.floor(math.sqrt(n))
    if root*root == n:
        if not suppress:
            print(f'{n} is a perfect square')
            print()
        return []

    num = 0
    denom = 1
    coef = root
    period = 0
    coefs_string = f"{coef}, ( "
    coefs = [coef]

    while True:
        num = denom*coef - num
        denom = (n - num*num) // denom
        coef = (root + num) // denom

        coefs.append(coef)
        coefs_string += str(coef)
        period += 1

        if coef == 2*root:
            coefs_string += ' )'
            if not suppress:
                print(f"sqrt({n}):")
                print("coefs =", coefs_string)
                print("period =", period)
                print()
            break
            
        coefs_string += ', '

    if not suppress:
        print()

    return coefs