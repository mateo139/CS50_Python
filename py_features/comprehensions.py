def main():
    yell("This", "is", "CS50")


def yell(*words):
    # list comprehensions
    uppercased = [word.upper() for word in words]
    print(*uppercased)

if __name__ == "__main__":
    main()
