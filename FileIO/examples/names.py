# name = input ("What's your name ?")
# file = open("names.txt", "a") # "a" - argument append
# file.write(f"{name}\n")
# file.close()

##name = input("What's your name ?")
##with open("names.txt", "a") as file:
##    file.write(f"{name}\n")

###with open ("names.txt", "r") as file:
###    lines = file.readlines()
###for line in lines:
###    print("hello,", line, end="")

####with open("names.txt", "r") as file:
####    for line in file:
####        print("hello,", line.rstrip())

#####with open("names.txt") as file:
#####    for line in sorted(file):
#####        print("hello,", line.strip())

names = []

with open("names.txt") as file:  # "r" - "read" argument is by default
    for line in file:
        names.append(line.rstrip())

for name in sorted(names, reverse=True):
    print(f"hello, {name}")
