import csv

name = input ("What's your name?")
home = input ("What's your home?")

with open ("students2.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})