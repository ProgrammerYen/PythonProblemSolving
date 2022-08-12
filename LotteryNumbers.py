from random import choice

six_numbers = []
list_numbers = list(range(1,50))
while True:
    number = choice(list_numbers)
    if number not in six_numbers:
        six_numbers.append(number)
        
    if len(six_numbers) == 6:
        break
    
six_numbers.sort()
print(six_numbers)

