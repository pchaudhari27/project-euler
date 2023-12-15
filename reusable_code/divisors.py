def find_all_divisors(num):
    divs = [1]
    i = 2
    while i*i <= num:
        if not num % i:
            divs.append(i)
        
        i += 1
    
    n = len(divs)
    for j in range(n)[::-1]:
        divs.append(num // divs[j])
    
    ret = []
    for d in divs:
        if d < num:
            ret.append(d)

    return ret