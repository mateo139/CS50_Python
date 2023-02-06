import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if type(s) != str:
        sys.exit()
    # place for input check, according to patterns below:
    # http://youtube.com/embed/xvFZjo5PgG0
    # https://youtube.com/embed/xvFZjo5PgG0
    # https://www.youtube.com/embed/xvFZjo5PgG0

    match = re.search("title", s)
    if match != None:
        pattern = '^.+src="(https?://(www)?.youtube.com/embed/.+)".+(title=).+$'
        #pattern = '^.+src="(.+)".+(title=).+$'
    else:
        pattern = '^.+src="(https?://(www.)?youtube.com/embed/.+)".+$'

    match = re.search(pattern, s)

    # if match:
    #    print("pattern found inside the string")
    # else:
    #    print("pattern not found")
    # return match.group(1)

    if match != None:
        conv_res = match.group(1).replace(
            "www.", "").replace("youtube.", "youtu.be").replace("com/embed", "").replace("http:", "https:")
        return (conv_res)
            # match = re.search("https", conv_res)
            # if match != None:
            #    pass
            # elif match




if __name__ == "__main__":
    main()
