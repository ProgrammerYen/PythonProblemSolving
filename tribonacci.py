def tribonacci(signature, n):
    #your code here
    if n < 3:
        return signature[:n]
    
    while len(signature) < n:
        signature.append(sum(signature[-3:]))
        
    return signature

print(tribonacci([1,1,1], 100))