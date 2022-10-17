#list of dictionaries
#list = []
#dict = {}
students = [
    {"name": "Mat", "school": "Politechnika", "city": "Wrocław"},
    {"name": "Pat", "school": "Politechnika", "city": "Legnica"},
    {"name": "George", "school": "Politechnika", "city": "Jawor"},
    {"name": "David", "school": None, "city": "Wrocław"},
]

for student in students:
    print(student["name"], student["school"], student["city"], sep=", ")