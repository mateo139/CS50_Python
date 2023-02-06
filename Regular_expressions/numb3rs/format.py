import re

# .+    => something
# ^     => at begining of users input
# $     => at the end of users input

name = input("What's your name? ").strip()
if matches := re.search(
    r"^(.+), *(.+)$", name
):  # := that assigns values to variables as part of a larger expression
    name = matches.group(2) + " " + matches.group(1)
    print(f"hello, {name}")

##matches = re.search(r"^(.+), *(.+)$", name)
##if matches:
##    name = matches.group(2) + " " + matches.group(1)
##print(f"hello, {name}")


### Lecture 7 - 1:25 min

# if "," in name:
#        last, first = name.split(", ")
#        name = f"{first} {last}"
# print(f"Hello, {name}")
