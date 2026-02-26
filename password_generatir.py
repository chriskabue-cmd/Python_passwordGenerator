import random
import string
#  generate a random password with a mix of uppercase, lowercase, digits, and symbols
#ask use the lenght of the passwords, if they want number or without numbers
def generate_password(min_lenght,numbers=True,special_characters=True):
    letters=string.ascii_letters
    digits=string.digits
    special=string.punctuation

    characters = letters
    if numbers:
        characters += digits
    if special_characters:
        characters += special
    password=""
    meets_criteria=False
    has_number=False
    has_special=False

    while not meets_criteria or len(password) < min_lenght:
        new_char=random.choice(characters)
        password += new_char

        if new_char in digits:
            has_number=True
        elif new_char in special:
            has_special=True
        meets_criteria=True
        if numbers:
            meets_criteria = has_number
        if special_characters:
            meets_criteria= meets_criteria and has_special
            
    return password 

# user gives the criteria for the password
min_length=int(input("Enter the minimum length of the password: "))
has_numbers=input("Include numbers? (y/n): ").lower() == "yes"
has_special=input("Include special characters? (y/n): ").lower() == "yes"
password=generate_password(min_length,has_numbers,has_special)
print(password)

