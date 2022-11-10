#sys.exit
#sys.argv[1]
#IndexError - list index ot of range if sys.argv[0]

import sys

if len(sys.argv) < 2:
    sys.exit("Too few arguments")

for name in sys.argv:
    print("hello, my name is", name)

#try:
#    print("hello, my name is", sys.argv[1])
#except IndexError:
#    print ("Too few arguments")


#if len(sys.argv) < 2:
#    sys.exit("Too few arguments")
#elif len(sys.argv) > 2:
#    sys.exit("Too much arguments")
#print("hello, my name is", sys.argv[1])