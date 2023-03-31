# docs.python.org/3/library/argparse.html
# python program_name.py -h -> present help
#                        -- help

import argparse

parser = argparse.ArgumentParser(description="Meow like a cat")
parser.add_argument("-n",default=1, help = "number of times to meow", type=int)
args = parser.parse_args()

for _ in range(args.n):
    print("meow")