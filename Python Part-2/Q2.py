def even(a,b):
    for i in range(a,b+1):
        if not i%2:
            print(i)

even(1,100000)