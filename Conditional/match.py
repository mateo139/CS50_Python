x = input ("What is the answer to the Great Question of Life, the Universe and Everything? ")
x = x.lower().strip(" ")
match x:
    case "42":
        print("Yes") #or return function
    case "forty-two":
        print ("Yes")
    case "forty two":
        print ("Yes")
    case _:
        print ("No")

