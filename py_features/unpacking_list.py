# first, _ = input ("What's your name ? ").split(" ")
# print(f"Hello {first}")

def total (dollars, zlotys, euros):
    return dollars * 5 + zlotys  + euros * 4

money = [100, 50, 25]

#print(total(money[0], money[1], money[2]), " PLN")

#UNPACKING LIST WITH A SINGLE ASTERISK *
print(total(*money), "PLN")