def rot13(message):
    encoded = ""
    message = list(message)
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    for i in message:
        if i.lower() in letters:
            if letters.index(i.lower()) + 13 < len(letters):
                if i.isupper():
                    encoded += letters[letters.index(i.lower()) + 13].upper()
                    
                else:
                    encoded += letters[letters.index(i) + 13]
                    
            else:
                if i.isupper():
                    encoded += letters[12 - (len(letters) - 1 - letters.index(i.lower()))].upper()
                    
                else:
                    encoded +=  letters[12 - (len(letters) - 1 - letters.index(i))]
                    
        else:
            encoded += i
            
    return encoded

print(rot13("uryyb ubj"))