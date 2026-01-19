n = int(input("Enter count of Elements: "))
list1 = []
for _ in range(n):
    list1.append(int(input()))

# list1 = set(list1)
print("-------------------------------------")
for i in range(len(list1)):
    if list1.count(i) > 1:
        print(i)    