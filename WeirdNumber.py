while True:
    n = input("Please choose a positive integer: ").strip()
    try:
        n = int(n)
        break
    
    except:
        print("Please try again.\n")
        
print()

if n % 2 == 1:
    print("Weird")
    
else:
    if n in range(2,6):
        print("Not weird")
        
    elif n in range(6,20):
        print("Weird")
        
    elif n > 20:
        print("Not weird")

        