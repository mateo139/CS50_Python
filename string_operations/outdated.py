import re

day = ""
month = ""
year = ""

months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December",
]

while True:
    date = input("Date: ").replace("/", " ").replace(",", " ").strip()
    date = re.sub(" +", " ", date).replace(" ", ",").split(",")

    month = date[0]
    if month in months:
        month = months.index(month) + 1
    else:
        month = int(month)
    if month > 12:
        continue
    month = str(month).zfill(2)  # another option to format "00" print(f"{n:02}")

    try:
        day = int(date[1])
        if day > 30:
            continue
        day = str(date[1]).zfill(2)  # another option to format "00" print(f"{n:02}")
    except ValueError:
        continue

    try:
        year = int(date[2])
        if len(date[2]) > 4:
            continue
        year = str(date[2]).zfill(2)  # another option to format "00" print(f"{n:02}")
    except ValueError:
        continue

    print(year, month, day, sep="-")
    break
