import sys
import json
import requests

if len(sys.argv) != 2:
    sys.exit("Missing command-line argument")

try:
    float(sys.argv[1])
except ValueError:
    sys.exit("Command-line argument is not a number")

response = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
o = response.json()
bitcoin_value = o["bpi"]["USD"]["rate"].replace(",", "")
bitcoin_value = float(bitcoin_value)
bitcoin_amount = float(sys.argv[1])
#print(type(bitcoin_amount))
print(f"${bitcoin_value * bitcoin_amount:,.4f}")


# print(int(sys.argv[1]) * o["bpi"]["USD"]["rate"])
# print(o.get("rate"))
