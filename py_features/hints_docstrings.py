# FORMAL RULES & CONVENTIONS FOR WRITING DOCUMENTATION
# peps/python.org/pep-0257/

def meow(n: int) -> str:
    """Explain here what funcion does"""
    
    """Meow n times.
        :param n: Number of times to meow
        :type n: int    
        :raise TypeError: If n is not an int
        :return: A string of n meows, one per line
        :rtype: str
    """

    return "meow\n" * n


number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="")
