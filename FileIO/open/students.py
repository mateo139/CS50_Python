# with open("names.csv") as file:
#    for line in file:
#        name, company = line.rstrip().split(",")
#        print(f"{name} is in {company.lstrip()}")

##with open("names.csv") as file:
##    for line in file:
##        row = line.rstrip().split(",")
##        print(f"{row[0]} is in {row[1].lstrip()}")

###students = []
###with open ("names.csv") as file:
###    for line in file:
###        name, company = line.rstrip().split(",")
###        students.append(f"{name} is in {company.lstrip()}")
###    for student in sorted(students):
###        print(student)

import csv

students = []

with open("names.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        students.append({"name": row["name"], "company": row["company"]})

"""
ALTERNATIVELY
    for name, company in reader:
        students.append({"name": name, "company": company})
"""
##    for line in file:
##        name, company = line.rstrip().split(",")
##        # student = {}
##        # student["name"] = name
##        # student["company"] = company.lstrip()
##        student = {"name": name, "company": company.lstrip()}
##        students.append(student)

"""
IF I DON'T USE LAMBDA A HAVE TO DEFINE SOME RETURN FUNCTIONS
def get_name(student):
    return student["name"]

def get_company(student):
    return student["company"]
"""

print(students)
"""
VARIANT 1
for student in sorted(students, key = get_company, reverse = False): # ??? get_company without "()"
    print(f"{student['name']} is in {student['company']}")
"""
"""
VARIANT 2 with lambda function
"""
for student in sorted(students, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['company']}")

#1:13 => csv.writer
