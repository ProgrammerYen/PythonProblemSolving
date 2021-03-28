def tower_builder(n_floors):
    # build here
    numCount = 1
    starCount = 0
    arr = []
    for i in range(1, n_floors + 1):
        arr.append(" " * (n_floors - numCount) + "*" * (i + starCount) + " " * (n_floors - numCount))
        numCount += 1
        starCount += 1
        
    for i in arr:
        print(i)

tower_builder(20)