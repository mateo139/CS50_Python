import sys
import os.path
from PIL import Image
from PIL import ImageOps

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")

if len(sys.argv) <= 2:
    sys.exit("Too few command-line arguments")

input_file = sys.argv[1]
output_file = sys.argv[2]

# Input check
i = sys.argv[1]
if os.path.isfile(i) == False:
    sys.exit("Input does not exist")

i = i.split(".")
# print(type(i[1]))
if i[1] != "jpg" and i[1] != "jpeg" and i[1] != "png":
    sys.exit("Invalid input")

# Output check
o = sys.argv[2]
# if os.path.isfile(o) == False:
#    sys.exit("Output does not exist")

o = o.split(".")
if o[1] != "jpg" and o[1] != "jpeg" and o[1] != "png":
    sys.exit("Invalid output")

# Input & Output extension similarity check
if i[1] != o[1]:
    sys.exit("Input and output have different extensions")

# Main program
try:
    shirt = Image.open("shirt.png")
    shirt = ImageOps.fit(
        method=Image.Resampling.BICUBIC, size=(1200, 1600), image=shirt
    )

    im = Image.open("before1.jpg")
    im.paste(shirt, mask=shirt)
    im.show()
    im.save(output_file)

except OSError:
    sys.exit("File can not be opened")
