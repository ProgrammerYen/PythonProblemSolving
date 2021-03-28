def findVowels(string):
    vowels = ["a", "e", "i", "o", "u"]
    vowelsFound = 0
    for i in list(string.strip().lower()):
        if i in vowels:
            vowelsFound += 1
            
    return vowelsFound

print(findVowels("ALUMINOSILICATES"))