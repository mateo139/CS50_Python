word = input ("Please input your text: ")
vowels_to_omitt = "AEIOUaeiou"
for v in vowels_to_omitt:
    word = word.replace(v, "")
print (word)
