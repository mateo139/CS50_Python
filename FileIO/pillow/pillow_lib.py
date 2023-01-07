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
        method=Image.Resampling.BICUBIC, size=(1200, 1200), image=shirt
    )

    im = Image.open("before1.jpg")
    im.paste(shirt, mask=shirt)
    im.show()
    im.save("after.jpg")

except OSError:
    sys.exit("File can not be opened")
