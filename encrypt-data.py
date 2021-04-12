import string
import random

def encrypt_data(data):
    shift_num = random.choice(list(range(1, 27)))
    
    data_values = [int(i) if i.isdigit() else i for i in data] # Saving values of the data given.
    data_values_shifted = []
    for i in data_values:
        if str(i).isalpha():
            letters = string.ascii_lowercase
            mask = letters[shift_num:] + letters[:shift_num]
            trantab = str.maketrans(letters, mask)
            data_values_shifted.append(i.translate(trantab))
            
        elif type(i) == int:
            data_values_shifted.append(str((i + shift_num) // shift_num))
            
        elif type(i) != int and not i.isalpha():
            data_values_shifted.append(i)
            
    return "".join(data_values_shifted) + " " + str(shift_num)