n = int(input("Enter count of Numbers: "))
data = []
for _ in range(n):
    data.append(int(input()))

tupeven = []
tupodd  = []
for i in data:
    if i%2:
        tupodd.append(i)
    else:
        tupeven.append(i)

tupeven = tuple(tupeven)
tupodd = tuple(tupodd)

print(f"Even tuple {tupeven}")
print(f"Odd tuple {tupodd}")
