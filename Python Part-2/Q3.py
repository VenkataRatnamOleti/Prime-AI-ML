n = int(input("Enter a number: "))
n = int(str(n)[::-1])

print("The digits are : ", end="")

while n > 0:
    print(n%10, end=" ")
    n //= 10

