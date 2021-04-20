def expanded_form(num):
    num = str(num)
    
    if len(num) < 2:
        return num
    
    partition = [str(int(num[i]) * 10 ** (len(num)-(i+1))) if i != len(num)-1 else num[i] for i in range(len(num))]
    partition = [i for i in partition if i != "0"]
    
    return " + ".join(partition)