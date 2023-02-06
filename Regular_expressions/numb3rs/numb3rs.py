# IT'S NICE TO KNOW
# IPv4 has dot-decimal notation #.#.#.#
# each hash# should be a number between 0-255 inclusive

# ENGLISH
# Suffice   - ENOUGH TO SAY
# akin      - "COUSIN OF ..."
# futher    - NEXT

import re
import sys
ip = ""


def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # pattern = "^a...s$"
    # pattern = "^.{1,3}\..{1,3}\..{1,3}\..{1,3}$"
    # pattern = "^[0-2][0-5][0-9]$"
    # pattern = "^(([0-2]?[0-9]?[0-5]?|[0-1]?[0-9]?[0-9]?)\.?){4,4}$"
    pattern = r"^([0]?[0-9]?[0-9]?|[1]?[0-9]?[0-9]?|[2]?[0-4]?[0-9]?|[2]?[5]?[0-5]?)\.([0]?[0-9]?[0-9]?|[1]?[0-9]?[0-9]?|[2]?[0-4]?[0-9]?|[2]?[5]?[0-5]?)\.([0]?[0-9]?[0-9]?|[1]?[0-9]?[0-9]?|[2]?[0-4]?[0-9]?|[2]?[5]?[0-5]?)\.([0]?[0-9]?[0-9]?|[1]?[0-9]?[0-9]?|[2]?[0-4]?[0-9]?|[2]?[5]?[0-5]?)$"
    result = re.match(pattern, ip)
    if result != None:
        result = True
    else:
        result = False
    return result
    # print (re.search("abc", "a", re.IGNORECASE))

    # print(matches)

    # if matches := re.search("[abc]", ip, re.IGNORECASE):
    #    return matches
    # print (matches)

    # matches = re.search("[abc]", ip, re.IGNORECASE)
    # print(matches)

    # if matches := re.search(r"^https?://(?:www\.)?twitter\.com/([a-z0-9_]+)", url, re.IGNORECASE):
    # print(f"Username:", matches.group(1))


if __name__ == "__main__":
    main()
