string = input("Enter String: ")
count = 0
for ch in string:
    if ch == " ":
        count+=1

print(f"No of Spaces are {count}")