#odd and even numbers

def main():
    x = int(input("What's x?"))
    if is_even(x):
        print("Even")
    else:
        print("Odd")

def is_even(n):
    #GENERAL SOLUTION
    #if n % 2 == 0:
    #    return True
    #else:
    #    return False

    #SPECYFIC "PYTHONIC" SOLUTION
    #return True if n % 2 == 0 else False

    #THE SIMPLEST SOLUTION
    return n % 2 == 0

main()