def fibonacci():
    fibNum = [0,1]
    while len(fibNum) != 100:
        fibNum.append(fibNum[-2] + fibNum[-1])
        
    return fibNum

fibNumbers = fibonacci()
print(fibNumbers)