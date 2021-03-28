def max_sequence(arr):
	# ... 
    if len(arr) == 0:
        return 0
    
    else:
        arr = list(set(arr))
        numMax = []
        for i in arr:
            if i == max(arr):
                numMax.append(i)
            
        numMax = numMax[:4]
        res = 0
        for i in numMax:
            res += i
            
        return res