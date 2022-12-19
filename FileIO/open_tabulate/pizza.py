import sys
from tabulate import tabulate
import csv

# This section check is CSV files exist and check if number of command arguments are proper

if len(sys.argv) > 2:
    sys.exit("Too many command-line arguments")

if len(sys.argv) == 1:
    sys.exit("Too few command-line arguments")

file_name = sys.argv[1]

m = sys.argv[1]
m = m.split(".")
if m[1] != "csv":
    sys.exit("Not a CSV file")

try:
    with open(file_name, "r") as file:
        file_reader = csv.reader(file, skipinitialspace=True, delimiter=",")
        # for row in file_reader:
        #    print(row)
        print(tabulate(file_reader, headers="firstrow", tablefmt="grid"))
except (FileNotFoundError):
    sys.exit("File does not exist")


# tablefmt = "grid"
# print(tabulate(table, headers, tablefmt="outline"))
