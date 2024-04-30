import random
import string

# ask the user for length
print("HELLO! HUMAN")
password_length = input("How long would you like your password to be?:")
password_length = int(password_length)

# pool of characters
characters = list((string.ascii_letters+string.digits+string.punctuation))
# shuffle characters
random.shuffle(characters)

# generate password
password = characters[0: password_length]

# print the password
generated_password = "".join(password)
print(f"Your password is {generated_password}")
