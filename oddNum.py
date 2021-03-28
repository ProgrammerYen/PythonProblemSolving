def oddNum(vector):
    arrLen = []
    [arrLen.append(i) for i in vector if i % 2 == 1]
    print(len(arrLen))
    
oddNum([1,3,4])