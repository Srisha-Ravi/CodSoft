#password generator
import random
import string

def password_generate(min_length,numbers=True,special_characters=True):
    letters = string.ascii_letters
    digits = string.digits
    special = string.punctuation

    char = letters
    if numbers:
        char += digits
    if special_characters:
        char += special

    passwrd = ""
    meet_critiria = False
    has_number = False
    has_special = False

    while not meet_critiria or len(passwrd) < min_length:
        new_char = random.choice(char)
        passwrd += new_char

        if new_char in digits:
            has_number = True
        elif new_char in special:
            has_special = True

        meet_critiria = True
        if numbers:
            meet_critiria = has_number
        if digits:
            meet_critiria = meet_critiria and has_special

    return passwrd

min_length = int(input("enter the length of the password = "))
has_number = input("do you want to include numbers (yes/no)? =").lower() == "yes"
has_special = input("do you want to include special characters (yes/no)? =").lower() == "yes"
passwrd = password_generate(min_length,has_number,has_special)
print("the generated password is = ",passwrd)
