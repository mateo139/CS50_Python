class Jar:
    def __init__(self, capacity=12):
        self._capacity = capacity
        self._size = 0

    def __str__(self):
        return self._size * "🍪"

    def deposit(self, n):
        self._size += n
        if self._size > self._capacity:
            raise ValueError

    def withdraw(self, n):
        self._size -= n
        if self._size < 0:
            raise ValueError

    @property
    def capacity(self):
        return self._capacity

    @property
    def size(self):
        return self._size


def main():
    jar = Jar()
    print("capacity:", jar.capacity)
    jar.deposit(4)
    print(jar.size)
    jar.withdraw(34)
    print(jar.__str__())


if __name__ == "__main__":
    main()
