import numpy as np

# bottom-up dynamic programming approach to partition an integer n
def partition(n):
    '''Given integer n, count the number of partitions of n, using numbers <= n. Dynamic programming approach.'''
    # initialize partitions
    partitions = [1] + [0]*n

    # for each iteration
    for i in range(1, n+1):
        # for every later partition
        for j in range(i, n+1):
            # how do previous partitions affect future partitions
            partitions[j] += partitions[j - i]

    # adjustment since we are only looking for solutions with >= 2 numbers
    return np.array(partitions)

# recurrence relation based on Euler's pentagonal number theorem, mathematically proven
# less intuitive but works faster
def partition_pentagonal(n):
    '''Given integer n, count the number of partitions of n, using numbers <= n. Euler's pentagonal number theorem approach.'''
    # intialize partitions
    partitions = [1] + [0]*n

    # initialzie pentagonal numbers and signs for the summation
    pentagonals = [0]
    signs = [0]
    k, sign = 1, 1
    while pentagonals[-1] < n:
        pentagonals.append(k*(3*k - 1) // 2)
        pentagonals.append(k*(3*k + 1) // 2)
        signs += [sign, sign]
        k += 1
        sign *= -1
    
    for x in range(1, n+1):
        # implement Euler's pentagonal number theorem
        # p(n) = sum(k) signs(k) * partition(x - pentagonals(k))
        # we can stop when x - pentagonals(k) < 0, since partition(n) = 0 when n < 0
        k = 1
        while pentagonals[k] <= x:
            partitions[x] += partitions[x - pentagonals[k]] * signs[k]
            k += 1
            if k >= len(pentagonals):
                break

    # adjustment since we are only looking for solutions with >= 2 numbers
    return np.array(partitions) - np.ones(n+1, int)