#                      Project: Password Strength Checker
#TODO-: Create a function check_password_strength() that:
#Asks the user to type a password.
#Checks if the password has at least:
#8 characters
#1 uppercase letter
#1 lowercase letter
#1 digit
#1 special character (e.g., @, #, $, !, etc.)
#Use conditionals in check_password_strength() to:

#TODO-: Check each requirement, and if the password meets all, print “Strong password.”
#TODO-: If any requirement isn’t met, print “Weak password” and mention what is missing.
#TODO-: Create a main() function that:
#TODO-: Calls check_password_strength().
#TODO-: Repeats the password check until the user decides to stop by typing "quit."
def check_password_strength():
    user_password = input("type you password: ")
    has_main_length = len(user_password) >= 8
    has_upper_case = any(char.isupper() for char in user_password)
    has_lower_case = any(char.islower() for char in user_password)
    has_digit = any(char.isdigit() for char in user_password)
    special_chars = "@#$!"
    has_special = any(char in special_chars for char in user_password)

    if has_main_length and has_upper_case and has_lower_case and has_digit and has_special:
        print("strong password")
    else:
        print("Weak password. Make sure it has:")
        if not has_main_length:
            print("- At least 8 characters")
        if not has_upper_case:
            print("- At least 1 uppercase characters")
        if not has_lower_case:
            print("- At least 1 lowercase characters")
        if not has_digit:
            print("- At least 1 digit")
        if not has_special:
            print("- At least 1 speical characters")

def main():
    check_password_strength()

while input("you want to check your password is this strong or not type yes: ").lower() == "yes":
    main()