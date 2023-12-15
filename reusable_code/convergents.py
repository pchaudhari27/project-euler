# find convergent based on continued fraction coefs
def convergents(series, cons_needed = 10, suppress = True):
    nums = []
    denoms = []
    for i in range(cons_needed):
        num, denom = 1, series[i]
        for j in range(1, i)[::-1]:
            next_num = series[j]
            num, denom = denom, next_num*denom + num
        
        if i > 0:
            num = series[0]*denom + num
        else:
            num, denom = denom, num

        nums.append(num)
        denoms.append(denom)
        
        if not suppress:
            print(f"n/d = {num} / {denom}")
            print()
    
    return nums, denoms
