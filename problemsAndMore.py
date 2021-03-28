def isValidSubsequence(array, sequence):
    # Write your code here.
    if sequence in list(range(min(array), max(array)+1)):
        return True
        
    else:
        return False

validSub = isValidSubsequence([1,2,3,4], [2,4])
print(validSub)