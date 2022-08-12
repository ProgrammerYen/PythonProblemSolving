def is_prime(n):
    factors = []
    for i in range(1, n+1):
        if n % i == 0:
            factors.append(i)
            
    return len(factors) == 2

def count_Kprimes(k, start, nd):
    k_primes = []
    for i in range(start, nd+1):
        factors = [j for j in range(1, i+1) if i % j == 0]
        primes = []
        for val in factors:
            if is_prime(val) == True:
                primes.append(val)
                
        if len(primes) == k:
            k_primes.append(i)
            
    return k_primes

print(count_Kprimes(3, 100, 1000))