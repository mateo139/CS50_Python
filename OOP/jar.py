class Jar:

    # size = 0
    # n = 0

    def __init__(self, capacity=12, size=0):
        self._capacity = capacity
        self._size = size

    def __str__(self):
        return self._size * "🍪"

    # deposit should add n cookies to the cookie jar. If adding that many would exceed the cookie jar’s capacity, though, deposit should instead raise a ValueError.
    def deposit(self, n):
        self._n = n
        self._size =  self._size + self._n

    def withdraw(self, n):
        self._n = n
        if self.size - self._n < 0:
            raise ValueError
        return self.size - self._n

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


jar = Jar()


#print(jar.size)
#print(jar.capacity)
#print(jar.__str__)
print(jar.deposit(10))
#print(jar.size)
#print(jar.__str__())
