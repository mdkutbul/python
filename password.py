

# FILE NAME - password.py

# NAME - Md Wara 
# DATE - 02/17/20223
# DESCRIPTION - generates random 8 characters password

import random
import string

def main():
    generatePassword()

def generatePassword():
 seed = int(input("Enter a seed for the random number generation: "))
 random.seed(seed)

 special_chars = "!@#$&(),-_"
 lowercase_letters = string.ascii_lowercase
 uppercase_letters = string.ascii_uppercase
 digits = string.digits


 password = (random.choice(special_chars) +
            random.choice(lowercase_letters) +
            random.choice(uppercase_letters) +
            random.choice(lowercase_letters) +
            random.choice(uppercase_letters) +
            random.choice(digits) +
            random.choice(digits) +
            random.choice(special_chars))
 print()
 print("Your random password is:", )
 print(password)

main()



