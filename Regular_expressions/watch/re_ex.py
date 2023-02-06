from re import search
txt = "The rain Spain in the "
x = search(r"\bS\w+", txt)
print(x.group())

# "\w" - Matches any alphanumeric character (digits and alphabets). Equivalent to [a-zA-Z0-9_]. By the way, underscore _ is also considered an alphanumeric character.
# "+" - The plus symbol + matches one or more occurrences of the pattern left to it.
# [] - 	A set of characters	example "[a-m]"