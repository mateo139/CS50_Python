def main():
    plate = input("Plate: ")
    if is_valid(plate) == True:
        print("Valid")
    else:
        print("Invalid")
    #start_with_two_letters(plate)

def is_valid(s):
    if start_with_two_letters(s) == True and number_of_characters(s) == True and numbers_in_middle(s) == True and special_marks(s) == True:
        return True

# #“All vanity plates must start with at least two letters.”
def start_with_two_letters(s):
    s = s[0:1].isalpha() and s[1:2].isalpha()
    return s

# #“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
def number_of_characters(plate):
    if len(plate)>=2 and len(plate)<=6:
        s = True
        return s
    else:
        s = False
        return s

# Numbers cannot be used in the middle of a plate; they must come at the end.
# For example, AAA222 would be an acceptable vanity plate; AAA22A would not be acceptable.
# The first number used cannot be a ‘0’.
def numbers_in_middle(plate):
    plate_full = plate
    for n in range (10):
        plate = plate.replace(str(n), "")
    x = len(plate)
    y = len(plate_full)
    plate_ending = plate_full[x:y]
    if len(plate_ending) == 0:
        return True
    elif plate_ending[0] == "0":
        return False
    else:
        for n in plate_ending:
            if n.isdigit() == True:
                return True
            else:
                return False
                break

#“No periods, spaces, or punctuation marks are allowed.”
def special_marks(plate):
    return plate.isalnum()

main()
