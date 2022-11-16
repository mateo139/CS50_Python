# https://pypi.org/project/inflect/
# pip install inflect
import inflect

p = inflect.engine()

names_list = []

try:
    while True:
        names_list.append(input("Name: "))

except (EOFError):
    print("\nAdieu, adieu, to ", p.join(names_list, final_sep=","), sep="")
