class Student:
    def check_pass_fail(self):
        if self.marks >= 40:
            return True
        else:
            return False
        
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks


student1 = Student("Mateo", 6)
student2 = Student("Zosia", 100)

# Defining atributes - not proper way...
# student1.name = "Mateo"
# student1.marks = 6

did_pass = student1.check_pass_fail()

did_pass = student1.check_pass_fail()
print(did_pass)
did_pass = student2.check_pass_fail()
print(did_pass)
