class Student:
    def __init__(self, name, roll_no, marks):
        self._name = name

        if(roll_no >= 1 and roll_no <= 100): self._roll_no = roll_no
        else: print("!Roll No between 1 and 100")
        
        if(marks>0): self._marks = marks
        else: print("!Marks Should be greater than 0.")

    def get_name(self):
        print(f"Name : {self._name}")
    
    def set_name(self, name):
        self._name = name

    def get_roll_no(self):
        print(f"Roll No : {self._roll_no}")

    def set_roll_no(self, roll_no):
        if(roll_no >= 1 and roll_no <= 100): self._roll_no = roll_no
        else: print("!Roll No between 1 and 100")

    def get_marks(self):
        print(f"Marks : {self._marks}")

    def set_marks(self, marks):
        if(marks>0): self._marks = marks
        else: print("!Marks Should be greater than 0.")

venkat = Student("Venkat",1,100)

venkat.get_name()
venkat.get_roll_no()
venkat.get_marks()
print("------------------")
venkat.set_name("Ratnam")
venkat.set_roll_no(95)
venkat.set_marks(99)
venkat.get_name()
venkat.get_roll_no()
venkat.get_marks()

