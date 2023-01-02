import sys
import csv
from itertools import islice
first_name = []
last_name = []
house = []
w = 0

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

m = sys.argv[1]
m = m.split(".")
if m[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(input_file) as file:
        for line in file:
            line = line.replace('"', "").replace('name', 'last,first')
            #print (line)
            last, first, hous = line.strip().split(',')
            first_name.append(first.lstrip())
            last_name.append(last)
            house.append(hous)
        #print(first_name)
        #print(last_name)
        #print(house)

    with open(output_file, "w", newline="") as out_file:
        writer = csv.writer(out_file, dialect='excel')
        #writer.writerow(["first" , "last" , "house"])
        for name in first_name:
            writer.writerow([first_name[w]] + [last_name[w]] + [house[w]])
            w += 1

except (FileNotFoundError):
    sys.exit("Could not read invalid_file.csv")
