def total(dollars, zlotys, euros):
    return dollars * 5 + zlotys + euros * 4


money = {"dollars": 100, "zlotys": 100, "euros": 100}

# UNPACKING A DICTIONARY WITH DOUBLE ASTERISK ** -> returning a pairs key:value
# print(total(money["dollars"], money["zlotys"], money["euros"]), "PLN")
print(total(**money), "zlotys")
