########################################################################
##
# CS 101 Lab
## Program #
# Name ABDALRAHMAN BASHIR
# Email bhbf73@umsystem.edu
##
# PROBLEM : Describe the problem
##
# ALGORITHM :
# 1. Write out the algorithm
##
# ERROR HANDLING:
# Any Special Error handling to be noted.  Wager not less than 0. etc
##
# OTHER COMMENTS:
# Any special comments
##
########################################################################


# import statements
from ast import While
# functions


def validate_user_input(user_input):
    if not (user_input.strip()):
        quit()
    if len(user_input) != 10:
        return (False, "Library card is invalid.\nThe length of the number given must be 10")
    if len(user_input) == 10:
        # check first five characters
        for i in range(5):
            if (user_input[i] < chr(65) or user_input[i] > chr(91)):
                return (False, "Library card is invalid.\nThe first 5 characters must be A-Z, the invalid character is at index "
                        + str(i) + " is " + user_input[i])
            # check character at index 5
        if (user_input[5] != '1' and user_input[5] != '2' and user_input[5] != '3'):
            return (False, "Library card is invalid.\nThe sixth character must be 1,2 or 3")
        if not (user_input[6] == '1' or user_input[6] <= '4'):
            return (False, "Library card is invalid.\nThe seven character must be 1,2,3 or 4")
        for i in range(7, 10):
            # check charactersn at index 7-9
            if user_input[i] < '0' or user_input[i] > '9':
                return (False, "Library card is invalid.\nThe last 3 characters must be 0-9, the invalid character is at index "
                        + str(i) + " is " + user_input[i])
        calculated_value = check_digit(user_input)
        given_value = int(user_input[9])

        if given_value != calculated_value:
            message = "Check digit " + str(given_value) + " does not match calculated value " \
                + str(calculated_value)
            return (False, message)
    return (True, "Library card is valid.")


def check_digit(user_input):
    sum = 0
    for i in range(len(user_input)):
        value = character_value(user_input[i])
        sum += value * (i+1)
    return sum % 10


def get_school(user_input):
    """"Assing index 5 to it respective school based on the value at that index """
    if user_input[5] == '1':
        return "School of Computing and Engineering SCE"
    elif user_input[5] == '2':
        return "School of Law"
    elif user_input[5] == '3':
        return "College of Arts and Sciences"
    else:
        return "Invalid School"


def get_grade(user_input):
    """"Assing index 6 to it respective school-year based on the value at that index """

    if user_input[6] == '1':
        return "Freshman"
    elif user_input[6] == '2':
        return "Sophomore"
    elif user_input[6] == '3':
        return "Junior"
    elif user_input[6] == '4':
        return "Senior"
    else:
        return "Invalid Grade"


def character_value(char):
    value = ord(char)
    if (value >= 48 and value <= 57):
        return value - 48
    elif (value >= 65 and value <= 90):
        return value - 65


if __name__ == "__main__":

    print("Main Program")
    user_input = "1"
    while (user_input.strip()):
        """main program will keep looping until until user_input is empty or whitespace"""
        user_input = input("Enter Library Card. Hit Enter to Exit ==> ")
        (is_valid, message) = validate_user_input(user_input)

        # if the return value from validate_user_input is true
        # then the functions check_digit, get_school get_grade will invoke.
        if is_valid == True:

            digit = check_digit(user_input)
            school = get_school(user_input)
            grade = get_grade(user_input)
            print(message)
            print("The card belongs to a student in " +
                  school)
            print("The card belongs to a " + grade)

        else:  # Otherwhise raise an Error and aske for valid input again
            print(message)
