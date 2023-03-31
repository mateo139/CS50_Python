def main():
    yell("This", "is", "CS50")


def yell(*words):
    # uppercased = []
    # for word in words:
    #    uppercased.append(word.upper())

    # mapping of function
    # map(function, iterable, ....)
    uppercased = map(str.upper, words)
    print(*uppercased)
    print (type(uppercased))


if __name__ == "__main__":
    main()
