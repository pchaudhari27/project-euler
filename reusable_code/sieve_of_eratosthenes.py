def sieve(n):
    arr = [0,0,1] + [1,0]*(n//2 + 1)
    i = 3
    while i*i <= n:
        if arr[i]:  
            arr[i*i::2*i] = [0]*len(arr[i*i::2*i])
        i += 2

    ret = []
    for (i, p) in enumerate(arr):
        if p:
            ret.append(i)

    return arr, ret