import re

# NICE TO KNOW ABOUT REGULAR EXPRESSIONS
# DOCUMENTATION: https://docs.python.org/3/library/re.html
# RE are for:
#   validating data
#   extracting data
#   cleaning up data

# metacharacters are:
# . ^ $ * + ? { } [ ] \ | ( )

# re.sub    (pattern, repl, string, count=0, flags=0)
# re.match  (pattern, string, flags=0)
# re.search (pattern, string, flags=0)
# re.split  (pattern, string, maxsplit=0, flags=0)
# re.findall (pattern, string, flags=0)

# raw string notation r"\n"

url = input("Username: ").strip()

if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    print(f"Username:", matches.group(1))
