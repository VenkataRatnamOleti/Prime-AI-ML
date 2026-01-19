data = dict()

def add():
    name  = input("Enter Student Name  : ")
    marks = int(input("Enter Student Marks : "))
    data.update({name:marks})
    print("Student added Successfully!")

def update_marks():
    name  = input("Enter Student Name         : ")
    marks = int(input("Enter new Marks for {name} : "))
    data.update({name:marks})
    print("Student updated Successfully!")

def search():
    name = input("Enter Student name: ")
    if name in data.keys():
        print(f"Student found!. {name} has {data[name]} marks")
    else:
        print("Student not found!")


def display():
    if len(data) == 0:
        print(f"No Data Available!")
        return
        
    for key,val in data.items():
        print(f"{key} has {val} marks")


while True:
    print("------------------------------------------")
    print("|   A - Add a student                    |")
    print("|   B - Update marks                     |")
    print("|   C - Search for a student             |")
    print("|   D - Display all students and marks   |")
    print("------------------------------------------")
    print()
    print("|--- Enter you Choice ---|>----> ",end="")
    
    choice = input()

    match choice:
        case 'A': add()
        case 'B': update_marks()
        case 'C': search()
        case 'D': display()
        case _: print("!Invalid option!")

    print()
    print()
    

