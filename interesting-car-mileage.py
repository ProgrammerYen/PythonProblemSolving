def is_interesting(number, awesome_phrases):
	# go to https://www.codewars.com/kata/52c4dd683bfd3b434c000292to see question.
    if len(str(number)) >= 3:
        if number in awesome_phrases or len(list(set(list(str(number))))) == 1:
            return 2
        
        num_count = 0
        num_count_2 = 0
        num_count_3 = 0
        for i in range(len(str(number))):
            if int(str(number)[i]) + 1 <= int(str(number)[i]):
                num_count += 1
                
            if int(str(number)[i]) - 1 >= int(str(number)[i]):
                num_count_2 += 1
                
            if str(number)[i:].count("0") == len(str(number)[i:]):
                num_count_3 += 1
                
        if num_count == len(str(number)) or num_count_2 == len(str(number)) or str(number)[::-1] == str(number)or num_count_3 == 1:
            return 2
        
        number += 1
        if number in awesome_phrases or len(list(set(list(str(number))))) == 1:
            return 1
        
        num_count = 0
        num_count_2 = 0
        num_count_3 = 0
        for i in range(len(str(number))):
            if int(str(number)[i]) + 1 >= int(str(number)[i]):
                num_count += 1
                
            if int(str(number)[i]) >= int(str(number)[i]):
                num_count_2 += 1
                
            if str(number)[i:].count("0") == len(str(number)[i:]):
                num_count_3 += 1
                
        if num_count == len(str(number)) or num_count_2 == len(str(number)) or str(number)[::-1] == str(number) or num_count_3 == 1:
            return 1
        
        number += 1
        if number in awesome_phrases or len(list(set(list(str(number))))) == 1:
            return 1
        
        num_count = 0
        num_count_2 = 0
        num_count_3 = 0
        for i in range(len(str(number))):
            if int(str(number)[i]) + 1 >= int(str(number)[i]):
                num_count += 1
                
            if int(str(number)[i]) >= int(str(number)[i]):
                num_count_2 += 1
                
            if str(number)[i:].count("0") == len(str(number)[i:]):
                num_count_3 += 1
            
        if num_count == len(str(number)) or num_count_2 == len(str(number)) or str(number)[::-1] == str(number) or num_count_3 == 1:
            return 1
        
    if len(str(number + 2)) >= 3:
        number += 1
        if number in awesome_phrases or len(list(set(list(str(number))))) == 1:
            return 1
        
        num_count = 0
        num_count_2 = 0
        num_count_3 = 0
        for i in range(len(str(number))):
            if int(str(number)[i]) + 1 >= int(str(number)[i]):
                num_count += 1
                
            if int(str(number)[i]) >= int(str(number)[i]):
                num_count_2 += 1

            if str(number)[i:].count("0") == len(str(number)[i:]):
                num_count_3 += 1
                
        if num_count == len(str(number)) or num_count_2 == len(str(number)) or str(number)[::-1] == str(number) or num_count_3 == 1:
            return 1
        
        number += 1
        if number in awesome_phrases or len(list(set(list(str(number))))) == 1:
            return 1
        
        num_count = 0
        num_count_2 = 0
        num_count_3 = 0
        for i in range(len(str(number))):
            if int(str(number)[i]) + 1 >= int(str(number)[i]):
                num_count += 1
                
            if int(str(number)[i]) >= int(str(number)[i]):
                num_count_2 += 1
                
            if str(number)[i:].count("0") == len(str(number)[i:]):
                num_count_3 += 1
                
        if num_count == len(str(number)) or num_count_2 == len(str(number)) or str(number)[::-1] == str(number) or num_count_3 == 1:
            return 1
        
    else:
        return 0

print(is_interesting(1329, [456, 908]))