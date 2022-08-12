def split_string(s):
    l = []
    for i in range(2, len(s)+1, 2):
        val = i
        if l != []:
            l.append(s[val-2: val])

        else:
            l.append(s[:val])

    if len(s) % 2 == 0:
        return l
    
    elif len(s) > 0:
        l.append(s[-1] + "_")
        return l