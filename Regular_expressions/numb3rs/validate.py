import re

email = input("what's your email ?").strip()

if re.search(r".+@.+\.edu", email): #r is raw strings
    print("Valid")
else:
    print("Invalid")
