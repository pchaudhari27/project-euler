def totient_sieve(n):
    if n < 2:
        print('totient function only applies to value > 2')
        return []

    arr = list(range(n+1))
    for m in arr[2:]:
        # if m is unchanged, it must be prime
        if arr[m] == m:
            # totient is m - 1
            arr[m] -= 1
            i = 2
            while m*i < n+1:
                # all other numbers with m as a factor need to be multiplied by (m-1)/m
                arr[m*i] = (arr[m*i]*m - arr[m*i]) // m
                i+=1

    return arr[2:]