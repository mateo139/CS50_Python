class Vault:
    def __init__(self, dolars=0, euros=0, plns=0):
        self.dolars = dolars
        self.euros = euros
        self.plns = plns

    def __str__(self):
        return f"{self.dolars} dolars, {self.euros} euros, {self.plns} PLN"


    def __add__ (self, other):
        dolars = self.dolars + other.dolars
        euros = self.euros + other.euros
        plns = self.plns + other.plns
        return Vault(dolars, euros, plns)

mateo = Vault(100, 200, 3000)
print(mateo)

maniek = Vault(1, 1, 1)
print(maniek)

total = mateo + maniek
print(total)

# dolars = mateo.dolars + maniek.dolars
# euros = mateo.euros + maniek.euros
# plns = mateo.plns + maniek.plns

# total = Vault(dolars, euros, plns)
# print(total)
