# Hints
# docs.python.org/3/library/re.html     =>  search.
# RE - special characters, per docs.python.org/3/library/re.html#regular-expression-syntax.
# Because backslashes in regular expressions could be mistaken for escape sequences (like \n), best to use Python’s raw string notation for regular expression patterns, else pytest will warn with DeprecationWarning: invalid escape sequence. Just as format strings are prefixed with f, so are raw strings prefixed with r. For instance, instead of "harvard\.edu", use r"harvard\.edu".
# Note that re.search, if passed a pattern with “capturing groups” (i.e., parentheses), returns a “match object,” per docs.python.org/3/library/re.html#match-objects, wherein matches are 1-indexed, which you can access individually with group, per docs.python.org/3/library/re.html#re.Match.group, or collectively with groups, per docs.python.org/3/library/re.html#re.Match.groups.
# Note that you can format an int with leading zeroes with code like    =>  print(f"{n:02}")
# wherein, if n is a single digit, it will be prefixed with one 0, per docs.python.org/3/library/string.html#format-string-syntax.

# English:
# recall - find sth in memory
# Deprecation Warning - warning concerning going back


import re
import sys


def main():
    # print(convert(input("Hours: ")))
    result = convert(input("Hours: "))

 #  print (f"{int(result[0]):02}", ":", f"{int(result[1]):02}", " to ", f"{int(result[3]):02}", ":", f"{int(result[4]):02}", sep = "")

    print(result)


def convert(s):
    if type(s) != str:
        sys.exit()
    result = []
    # pattern = '^.+src="(https?://(www.)?youtube.com/embed/.+)".+$'
    # pattern = '^([0]?[0-9]|[1][0-2])(:| )?([0-5][0-9])?( )?(AM|PM)?$'
    # pattern = r'^([0]?[0-9]|[1][0-2])(:| )?([0-5][0-9])?( )?(AM|PM)? to ([0]?[0-9]|[1][0-2])(:| )?([0-5][0-9])?( )?(AM|PM)?$'
    pattern = r'^([0]?[0-9]|[1][0-2])(:| )?([0-5][0-9])?( )(AM|PM)? to ([0]?[0-9]|[1][0-2])(:| )?([0-5][0-9])?( )(AM|PM)?$'
    match = re.search(pattern, s)
    if match == None:
        raise ValueError
    hours1 = match.group(1)
    minutes1 = match.group(3)
    time1 = match.group(5)
    hours2 = match.group(6)
    minutes2 = match.group(8)
    time2 = match.group(10)
    result = [hours1, minutes1, time1, hours2, minutes2, time2]
    if match == None:
        raise ValueError
    result[0] = int(result[0])
    if result[0] == 12 and result[2] == "AM":
        result[0] = 0
    if result[1] != None:
        result[1] = int(result[1])
    else:
        result[1] = 0
    result[3] = int(result[3])
    if result[4] != None:
        result[4] = int(result[4])
    else:
        result[4] = 0
    if result[2] == "PM":
        result[0] = int(result[0]) + 12
    if result[3] == 12 and result[5] == "PM":
        result[3] == 12
    elif result[5] == "PM":
        result[3] = int(result[3]) + 12
    result = (f"{result[0]:02}" + ":" + f"{result[1]:02}" + " to " +
              f"{result[3]:02}" + ":" + f"{result[4]:02}")
    return result


if __name__ == "__main__":
    main()
