def arrayDiff(a, b):
    for i in range(len(a)-1):
        for j in range(i+1, len(a)):
            if a[i] == a[j]:
                a.remove(a[j])
    
    if len(b) != 0:
        b = [str(i) for i in b]
        b = int("".join(b))
        
    if b in a: 
        a.remove(b)
        return a
    
    elif len(b) == 0:
        return a
    
    elif b not in a and len(b) != 0:
        b = []
        return b
        

arrDifference = arrayDiff([1,2,2], [2])
print(arrDifference) 