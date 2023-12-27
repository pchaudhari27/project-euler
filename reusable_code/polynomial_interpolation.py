import numpy as np

# Newton's method based on forward differences
# implement divided differences (forward differencing) for newton's coefficients
def divided_differences(xs, ys):
    if len(xs) != len(ys):
        raise ValueError('Mismatching data points: number of xs needs to match number of ys')
    
    k = len(ys)
    coefs = [ys[0]]
    differences = ys.copy()

    for i in range(1, k):
        new_differences = []
        for j in range(1, len(differences)):
            new_differences.append((differences[j] - differences[j-1])/(xs[j+i-1] - xs[j-1]))
        
        differences = new_differences.copy()
        coefs.append(differences[0])
    
    return np.array(coefs)
    

# interpolate based on k points, and plug in n, or pre-calcualte coefficients
def newton_polynomial(xs, ys, n, coefs = None):
    if coefs is None:
        coefs = divided_differences(xs, ys).copy()
    s = coefs[0]
    for i in range(1, len(coefs)):
        prod = 1
        for j in range(i):
            prod *= n - xs[j]

        s += coefs[i]*prod

    return s