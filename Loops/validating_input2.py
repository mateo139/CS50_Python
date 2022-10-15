def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n ? "))
        if n > 0:
            return n


def meow(n):
    for _ in range (n): #Basically it means you are not interested in how many times the loop is run till now just that it should run some specific number of times overall
        print ("meow")

main()