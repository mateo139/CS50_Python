name = input("Put here \"camel\" name: ")

list =[]

for n in name:
    if n.isupper() == True:
        n = "_" + n.lower()
        print(n, end="\n")
    list.append(n)
#print (list)

name = "".join(list)
print(name)
