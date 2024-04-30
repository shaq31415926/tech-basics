import random
import string

print("HELLO! HUMAN")
password_length = int(input("How long would you like your password to be?:"))

# pool of characters
characters = list((string.ascii_letters+string.digits+string.punctuation))
# shuffle characters
random.shuffle(characters)

# generate password
password = characters[0: password_length]

# print the password
generated_password = "".join(password)
print(f"Your password is {generated_password}")