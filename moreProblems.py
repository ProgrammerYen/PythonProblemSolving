def pal_seq(num):
    count = 0
    rangeNum = list(range(1, (num//2)+2))
    for i in rangeNum:
        i2 = i
        while i2 + int(str(i2)[::-1]) != num:
            i2 = int(i2) + int(str(i2)[::-1])
            
            if i2 > num:
                break
            
            count += 1
            
            if i2 == num:
                return (i, count)
        
        
print(pal_seq(4884))
            