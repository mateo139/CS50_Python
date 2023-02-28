class Engineer:
    def __init__(self, name):
        if not name:
            raise ValueError("Missing name")
        self.name = name

class Man (Engineer):
    def __init__(self, name, id):
        super().__init__(name)
        self.id = id

class Leader (Engineer):
    def__init__(self, name, skill):
        super().__init__(name)
        self.skill = skill

engineer = Engineer ("Grzegorz")
man = Man ("Mateusz", "007")
leader = Leader ("Krzysztof", "management")
