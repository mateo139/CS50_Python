name = input ("What is your name? ").strip().title()

#name = name.strip()
#name = name.title()
#name = name.strip().title()

first, last = name.split(" ")

print (f"hello, {last}")