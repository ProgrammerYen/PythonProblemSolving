def beeramid(bonus, price): # O(n)
    number = 1
    num_count = 0
    while bonus >= (number ** 2) * price:
        num_count += 1
        bonus -= (number ** 2) * price
        number += 1
        
    return num_count

print(beeramid(23098, 23))