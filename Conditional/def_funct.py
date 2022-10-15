def main ():
    text = input ("Hello, please enter your text ")
    print (convert (text))


def convert (text):
    #text = text.replace(":)", "🙂")
    #text = text.replace(":(", "🙁")
    return text.replace(":)", "🙂").replace(":(", "🙁")

main ()
