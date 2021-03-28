def compound_match(words, target):
    for i in range(len(words)):
        for j in range(len(words)):
            if words[i] + words[j] == target:
                return [words[i], words[j], [words.index(words[i]), words.index(words[j])]]
            
            elif words[j] + words[i] == target:
                return [words[i], words[j], [words.index(words[j]), words.index(words[i])]] 
            
print(compound_match(['bel', 'bed', 'low', 'grab', 'be', 'knight'], "bellow"))