menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

total = 0

try:
    while True:
        key = input("Item:").title()
        #print(key)
        if key in menu:
            total += menu[key]
            print ("Total: $",format(total,".2f"), sep="")
except (EOFError, KeyError):
    pass



#while True:
#    try:
#        order = menu.get(input("Item:"))
#        total =+ order
#        print ("Total: $",total)
#    except EOFError:
#        break



