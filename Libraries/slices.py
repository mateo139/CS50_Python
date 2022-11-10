#sys.argv is a list [name_of_program, 1st element, 2nd element, ....]
import sys

print(sys.argv)

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv[1:]:
    print("hello, my name is", name)