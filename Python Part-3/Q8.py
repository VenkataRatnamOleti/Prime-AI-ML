n = int(input("Enter count of List-1 Elements: "))
list1 = []
for _ in range(n):
    list1.append(int(input()))


n = int(input("Enter count of List-2 Elements: "))
list2 = []
for _ in range(n):
    list2.append(int(input()))

list1 = set(list1)
list2 = set(list2)

list1 = list1.intersection(list2)

print(f"Common elements are {list1}")