def mixed_fraction(s):
    splitted_num = [int(i) for i in s.split("/")]
    
    fnum_sub = ""
    
    if str(splitted_num[0])[0] == "-" and str(splitted_num[-1])[0] == "-":
        n = int(str(splitted_num[0])[1:])
        d = int(str(splitted_num[-1])[1:])
    
    elif str(splitted_num[0])[0] == "-" and str(splitted_num[-1])[0] != "-":
        fnum_sub = "-"
        n = int(str(splitted_num[0])[1:])
        d = splitted_num[-1]
        
    elif str(splitted_num[0])[0] != "-" and str(splitted_num[-1])[0] == "-":
        fnum_sub = "-"
        n = splitted_num[0]
        d = int(str(splitted_num[-1])[1:])
    
    else:
        n = splitted_num[0]
        d = splitted_num[-1]
    
    fact_n = []
    fact_d = []
    for i in range(1, n+1):
        if n % i == 0:
            fact_n.append(i)
            
    for i in range(1, d+1):
        if d % i == 0:
            fact_d.append(i)
    
    common_fact = [i for i in fact_n if i in fact_d]
    if len(common_fact) > 0:
        n = n / max(common_fact)
        d = d / max(common_fact)
    
    whole_num = n // d
    fraction = n % d
    
    if fraction == 0:
        return fnum_sub + str(int(whole_num))
    
    if whole_num == 0:
        return fnum_sub + str(int(fraction)) + "/" + str(int(d))
    
    mixed = fnum_sub + str(int(whole_num)) + " " + str(int(fraction)) + "/" + str(int(d))
    return mixed

print(mixed_fraction("-645/-389"))