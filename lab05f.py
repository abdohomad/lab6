########################################################################
##
## CS 101 Lab
## Program #
## Name
## Email
##
## PROBLEM : Describe the problem
##
## ALGORITHM : 
##      1. Write out the algorithm
## 
## ERROR HANDLING:
##      Any Special Error handling to be noted.  Wager not less than 0. etc
##
## OTHER COMMENTS:
##      Any special comments
##
########################################################################


# import statements

# functions
def valid_user_input(string_input):
    while true:
        if len(string_input) != 10:
            print ("Libray card is invalid")
        elif len(string_input) == 10:
            for i in range(0, 5):
                if not(string_input[i].isupper()):
                    print ("Libray card is invalid")

            for i in range(len(string_input)):
                if not (string_input[5] == 1 or string_input[5] == 2 or string_input[5] == 3):
                    print ("Libray card is invalid")
                elif not (string_input[6] == 1 or string_input[6] == 2 or string_input[6] == 3 or string_input[6] == 4):
                    print ("Libray card is invalid")

            for i in range(string_input[7:9]):
                if not(string_input[i] == range(0, 9)):
                    print ("Libray card is invalid")
        else:

            return string_input

def check_digit():

    user_input = input("Enter Library Card. Hit Enter to EXit")

    user_input = valid_user_input(user_input)


def get_school():


def get_grade():


if __name__ == "__main__":

    # main program
    check_digit()
    print("Main Program")

