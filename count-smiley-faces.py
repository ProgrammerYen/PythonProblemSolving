def count_smileys(arr):
    count_smile = 0
    for i in arr:
        if i[0] == ":" or i[0] == ";":
            if i[1] == ")" or i[1] == "D":
                count_smile += 1
                
            elif i[1] == "~" or i[1] == "-" and (i[2] == ")" or i[2] == "D"):
                count_smile += 1
                
    return count_smile