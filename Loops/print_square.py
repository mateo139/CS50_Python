def main():
    print_square(3)

def print_square(size):
    for i in range(size):
        print_row(size)
        
        #print("#" * size)
                
        ##for j in range (size):
        ##    print("#", end="")
        ##print()

def print_row(width):
    print("#" * width)

main()