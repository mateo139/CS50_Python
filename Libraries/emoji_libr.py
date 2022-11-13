# succinctly "pip install emoji"
# https://pypi.org/project/emoji/

import emoji

input_words = input("Input: ")

print(emoji.emojize("Output:" + input_words, language="alias"))
