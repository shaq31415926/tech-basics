import os

# code to clear the screen
os.system("clear")
print("Hello! This is my calculator in Python")

num1 = input("Please enter the first number:")

# convert the variables to float, otherwise Python will not recognise them as numbers
# and if you want to make sure the user only enters a digit, you can add some logic that keeps looping until the user
while True:
    try:
        num1 = float(num1)
        break
    except:
        num1 = input("PLEASE ENTER A NUMBER:")

operator = input("Please enter the operator (+, -, x, /):")
num2 = input("Please enter the second number:")


while True:
    try:
        num2 = float(num2)
        break
    except:
        num2 = input("PLEASE ENTER A NUMBER:")


# the if else-if satement that calculates what the user enters
if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "x":
    total = num1 * num2
elif operator == "/" and num2 > 0:
    total = num1 / num2
else:
    total = "Math Error"

print(f"The answer is {total}")
