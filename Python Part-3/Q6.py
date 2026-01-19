words = ["apple", "banana", "kiwi", "cherry", "mango"]
data = {}
for word in words:
    data.update({word:len(word)})

for key, val in data.items():
    print(f"{key} : {val}")