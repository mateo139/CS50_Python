def main():
    time = input("What time is it ? Please type time in format #:## or ##:##")
    time = convert (time)
    #print(time)
    if time >= 7.00 and time <= 8.00:
        print("breakfast time")
    elif time >= 12.00 and time <= 13.00:
        print("lunch time")
    elif time >= 18.00 and time <= 19.00:
        print("dinner time")
    else:
        pass

def convert(time):
    hour, minutes = time.split(":")
    hour = float(hour)
    #if minutes > 59:
    #    print("Type proper value. Minutes may by max 59")
    #    pass
    minutes = float (minutes)
    minutes = minutes / 60
    time = hour + minutes
    return time



if __name__ == "__main__":
    main()
