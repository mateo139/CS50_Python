#students = ["Dave", "George", "Mike", "Stan"]
#schools = ["Harvard", "Oxford", "Politechnika", "Hogwart"]

students = {
    "Dave": "Harvard",  #1st keys
    "George": "Oxford",
    "Mateo": "Politechnika",
    "Harry": "Hogwart",
}

#print(students["Dave"])
#print(students["George"])
#print(students["Mike"])
#print(students["Stan"])

for student in students:
    print(student, students[student], sep=", ")