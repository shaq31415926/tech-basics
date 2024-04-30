import random
import string

# This code was inspired by Marcel

print("HELLO! HUMAN")
# ask the user for input
letters_length = int(input("How many letters would you like in your password?:"))
digits_length = int(input("How many digits would you like in your password?:"))
punctuation_length = int(input("How many punctuations would you like in your password?:"))

# create a pool of letters, digits and punctuations
letters = list(string.ascii_letters)
random.shuffle(letters)
digits = list(string.digits)
random.shuffle(digits)
punctuation = list(string.punctuation)
random.shuffle(punctuation)

# create a password based on the users input
password = letters[0:letters_length] + digits[0: digits_length] + punctuation[0: punctuation_length]
# shuffle password
random.shuffle(password)

# print the password
generated_password = "".join(password)
print(f"Your password is of length {len(password)} and is: {generated_password}")

