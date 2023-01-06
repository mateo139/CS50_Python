from PIL import (
    Image,
    ImageOps,
)
import sys


try:
    shirt = Image.open("shirt.png")
    # print(shirt.format, shirt.size, shirt.mode)
    # shirt.show()
    shirt = ImageOps.fit(
        method=Image.Resampling.BICUBIC, size=(1200, 1600), image=shirt
    )

    im = Image.open("before1.jpg")
    # print(im.size)
    im.paste(shirt, mask=shirt)
    im.show()

except OSError:
    sys.exit("File can not be opened")
