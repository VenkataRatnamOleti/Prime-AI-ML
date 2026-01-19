data = []

n = int(input("Enter no of elements: "))

print(f"Enter {n} elements:")
for _ in range(n):
    data.append(int(input()))

print(f"Averate is {sum(data)/n}")