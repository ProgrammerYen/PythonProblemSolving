def duplicate_encode(word):
    #your code here
    word = list(word)
    word = [i.lower() for i in word]
    wordEncode = ""
    for i in word:
        if word.count(i) > 1:
            wordEncode += ")"
            
        else:
            wordEncode += "("
            
    return wordEncode

print(duplicate_encode("(ObuyGFuJHOyGFGdFGT)v!OQ JQFQbGGFOPScJ!a"))
