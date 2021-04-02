import math
def list_squared(m, n):
    perfect_squares = []
    for i in range(m, n+1):
        square_factors = [j ** 2 for j in range(1, i+1) if i % j == 0]
        if math.sqrt(sum(square_factors)).is_integer():
            perfect_squares.append([i, sum(square_factors)])
            
    return perfect_squares

print(list_squared(23, 1000))