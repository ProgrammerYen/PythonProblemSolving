string = input("Please enter a word or number: ").strip().lower()

def checkPalindrome(palinString):
    if string == string[::-1]:
        return "The input that you entered is a palindrome"
    
    else:
        return "The input that you entered is not a palindrome"

print(checkPalindrome(string)) 