def Fibonacci(n):
    fibNum = [0,1]
    
    if n <= 1:
        fibNum = [0]
    
    while len(fibNum) != n and n >= 3:
        fibNum.append(fibNum[-2] + fibNum[-1])
                      
    return fibNum

print(Fibonacci(2.5)) 

    