from PIL import Image
import sys

try:
    im = Image.open("before1.jpg")
    print(im.format, im.size, im.mode)
    im.show()
except OSError:
    sys.exit("File can not be opened")

