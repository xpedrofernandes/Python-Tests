# LABTEST 1 - PEDRO FERNANDES (D23124885)
# PASSWORD CHECKER

# if password entered is not valid, strengthen it
# the criteria for the password to be valid is:
# a) at least length 10; b) at least one numerical value;
# c) at least one upper case value; d) at least one special character (not letter or number)

import random
import string

# function to check is the password is valid
def is_valid(password):
    num_value = False # keep track if a numeric value is in the string
    upper_value = False # keep track if an uppercase value is in the string
    special_value = False # keep track if a special character is in the string

    if len(password) < 10: # check if size is at least 10
        return False
    else:
        for p in password: # iterate through the password
            if p.isnumeric(): # check if p is numeric
                num_value = True # update tracker

            if p.isupper(): # check if p is uppercase
                upper_value = True # update tracker

            if not p.isalnum(): # check if p is special
                special_value = True # update tracker

    # if there is no numeric OR no uppercase OR no special, return false
    if num_value == False or upper_value == False or special_value == False:
        return False
    else: # if all criteria met, return true
        return True


# function to strengthen the password
def strengthen_password(password):
    strong_password = password # new password starts as the old one
    num_value = False # tracker numeric
    upper_value = False # tracker uppercase
    special_value = False # tracker special

    for p in password:
        if p.isnumeric():  # check if p is numeric
            num_value = True

        if p.isupper():  # check if p is uppercase
            upper_value = True

        if not p.isalnum():  # check if p is special
            special_value = True


    if upper_value == False: # if there are no uppercase values, add upper char
        upper_case = random.choice(string.ascii_uppercase)
        strong_password += upper_case

    if num_value == False: # if there are no numeric values, add num
        digit = random.choice(string.digits)
        strong_password += digit

    if special_value == False: # if there are no special values, add special char
        special_char = random.choice(string.punctuation)
        strong_password += special_char

    if len(strong_password) < 10: # if length of password is less than 10, keep adding chars until it reaches 10
        while len(strong_password) < 10:
            random_char = random.choice(string.ascii_letters + string.digits)
            strong_password += random_char

    return strong_password # return strengthen password

def main():
    user_input = ""

    while user_input != "exit": # loop until 'exit' is entered
        user_input = input("Enter a password for evaluation (or type 'exit' to quit): ") # get user input
        if user_input == "exit":
            return
        elif is_valid(user_input): # check if input is a valid password by calling function
            print("Password is valid.")
        else:
            print("Password is not valid.")
            print("New suggested password: ", strengthen_password(user_input)) # recommend strengthen password

if __name__ == "__main__":
    main()