def namelist(names):
    if len(names) == 0: 
        return ""
    
    formatted = [i["name"] + "," for i in names]
    print(*formatted[:-2], formatted[-2][:-1], "&", formatted[-1][:-1])

namelist([{'name': 'Bart'},{'name': 'Lisa'},{'name': 'Maggie'},{'name': 'Homer'},{'name': 'Marge'}])