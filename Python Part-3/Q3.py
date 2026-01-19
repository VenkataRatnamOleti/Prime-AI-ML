n = int(input("Enter count of 1st List: "))
print(f"Enter {n} elements: ")
list1 = []
for _ in range(n):
    list1.append(int(input()))

n = int(input("Enter count of 1st List: "))
print(f"Enter {n} elements: ")
list2 = []
for _ in range(n):
    list2.append(int(input()))

print(f"First List {list1}")
print(f"Second List {list2}")
print(f"Merged List {list1+list2}")
# print(f"Sorted Merged List {sorted(list1+list2)}")
list1 = list1+list2
list1.sort()
print(f"Sorted Merged List {list1}")
