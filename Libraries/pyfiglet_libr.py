# pip install pyfiglet==0.7
from pyfiglet import Figlet
import random
import sys

# figlet.setFont(font = "3-d")
# print(figlet.renderText(sentence))

figlet = Figlet()
font_list = figlet.getFonts()

if len(sys.argv) < 3:
    sys.exit("Invalid usage")

elif (sys.argv[1] == "-f" or sys.argv[1] == "--font") and sys.argv[2] in font_list:
    sentence2 = input("Input: ")
    figlet.setFont(font=sys.argv[2])
    print(figlet.renderText(sentence2))

elif sys.argv[1] == "0":
    sentence1 = input("Input: ")
    figlet.setFont(font=font_list[random.randint(0, 418)])
    print(figlet.renderText(sentence1))

elif sys.argv[1] != "-f" or sys.argv[1] != "--font":
    sys.exit("Invalid usage")

else:
    sys.exit("Invalid usage")
