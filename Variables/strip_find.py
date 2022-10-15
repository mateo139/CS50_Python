greeting = input ("What is your greeting ?")
greeting = greeting.strip().lower()

if "hello" in greeting:
    print ("$0")

elif greeting.find("h") == 0:
    print ("$20")

#if greeting.find("h") == 0:
#    print (True)
#else:
#    print (False)

else:
    print ("$100")

