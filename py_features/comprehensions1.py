workers = [
    {"name": "Mateo", "job": "IT_in_engineering"},
    {"name": "Bill", "job": "R&D"},
    {"name": "Georg", "job": "R&D"},
    {"name": "Tomas", "job": "R&D"},
]

# LIST OF COMPREHENSION , very specyfic "Pythonic" way of writing code
research_and_dev  =[
    worker["name"] for worker in workers if worker["job"] == "R&D"
] 

for worker in sorted(research_and_dev):
    print(worker)