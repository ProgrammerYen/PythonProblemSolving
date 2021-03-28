# Assuming the length of both arguments are equal.
def sumList(l1, l2):
    l3 = []
    index = 0
    while index != len(l1):
        l3.append(l2[index])
        l3.append(l1[index])
        index += 1
    return l3

print(sumList([1,2,3], ["a", "b", "c"]))