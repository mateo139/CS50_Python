from datetime import date
import datetime
import sys
import inflect

p = inflect.engine()


def main():

    try:
        timedelta_words = convert(
            input("What is your B'day? (in YYYY-MM-DD) "))
        print(timedelta_words)

    except:
        sys.exit("Invalid value")


def convert(birthday):
    birthdate = datetime. datetime. strptime(birthday, "%Y-%m-%d"). date()
    today = date.today() # datetime.date(year = 2000, month = 1, day = 1)
    timedelta = today - birthdate
    # print("birthday = ", birthday)
    # print("birthdate = ", birthdate)
    # print("timedelta = ", timedelta)
    # print("today = ", today)

    timedelta = timedelta.total_seconds() / 60
    # print(timedelta)

    timedelta = int(timedelta)
    timedelta_words = p.number_to_words(
        timedelta, andword="").capitalize() + " minutes"
    return timedelta_words


if __name__ == "__main__":
    main()
