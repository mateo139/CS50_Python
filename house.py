#MATCH

name = input("What's your name?")

#if name == "Harry" or name == "Hermione" or name == "Ron":
#    print("Gryffindor")
#elif name == "Draco":
#    print("Slytherin")
#else:
#    print("Who?")

match name:
    case "Harry" | "Hermione" | "Ron" :
        print ("Gryffindor")
    #case "Harry":
    #    print ("Gryffindor")
    #case "Hermione":
    #    print ("Gryffindor")
    #case "Ron":
    #    print ("Gryffindor")
    case "Draco":
        print ("Slytherin")    
    #all other cases
    case _:
        print ("Who?")