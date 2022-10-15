#x =  input("What's x?")
#y =  input("What's y?")
#z = int(x) + int(y)
#print (z)

#x = int(input("What's x?"))
#y = int(input("What's y?"))
#print (x + y)

#x = float (input("What's x ?"))
#y = float (input("What's y ?"))
##z = round(x + y)
#z = x / y
#print (z)
#print(f"{z:,}")
##z = round(x / y, 2)
##print(f"{z:.2f}")

def main():
    x = int(input("What's x?"))
    print("x squared is", square(x))

def square(n):
    #return n * n
    ##return pow(n, 2)
    return n ** 2

main ()
    