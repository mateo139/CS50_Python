class Jar:

    def __init__(self, capacity=12):
        # if capacity < 0:  # or type(capacity) not int
        #    raise ValueError
        self._capacity = capacity
        self._cookies = 0

    def __str__(self):
        return self._cookies * "🍪"
    

    # def __str__(self, n):
    #    self.n = n
    #    if type(n) != int:
    #        return ""
    #    return self.n * "🍪"

    # def deposit(self, n):
    #    self.n = n
    #    self.cookies = cookies
    #    cookies = cookies + n
    #    return cookies

    # def withdraw(self, n):
    #    cookies_amount = cookies_amount - n
    #    if cookies_amount < 0:
    #       raise ValueError
    #
    @property
    def capacity(self):
        return self._capacity

    @property
    def cookies(self):
        return self._cookies



jar = Jar(10)
print(jar)
print(jar.capacity)

