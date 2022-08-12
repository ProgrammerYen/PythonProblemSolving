def sum_dig_pow(a, b):
    sum_dig_consec = []
    for i in range(a, b+1):                         
        if sum([int(list(str(i))[j]) ** (j + 1) for j in range(len(list(str(i))))]) == i:
            sum_dig_consec.append(i)
        
    return sum_dig_consec