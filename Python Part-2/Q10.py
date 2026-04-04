n = 5

while True:
    a = int(input("Guess the Number: "))
    if a < n:
        print("Too low")
    elif a > n:
        print("Too high")
    else : 
        print("Correct!")
        break