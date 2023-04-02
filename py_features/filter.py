workers = [
    {"name": "Mateo", "job": "engineer"},
    {"name": "Bill", "job": "mechanic"},
    {"name": "Georg", "job": "mechanic"},
    {"name": "Tomas", "job": "mechanic"},
]


def is_mechanic(s):
    return s["job"] == "mechanic"

mechanics = filter(is_mechanic, workers)

for mechanic in sorted (mechanics, key=lambda s: s["name"]):
    print (mechanic["name"])
