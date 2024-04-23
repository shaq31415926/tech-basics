num1 = input("What is the first number?:")
while True:
    # check if num1 can be converted to a float
    try:
        num1 = float(num1)
        break
    # if num1 can not be converted to a float then ask the user to enter a number
    except:
        num1 = input("PLEASE ENTER A NUMBER:")

operator = input("What operator would you like (+, -, *, /):")
print(operator)

while operator not in ["+", "-", "*", "/"]:
        operator = input("SELECT THE CORRECT OPERATOR:")

num2 = input("What is the second number?:")
while True:
    # check if num1 can be converted to a float
    try:
        num2 = float(num2)
        break
    # if num1 can not be converted to a float then ask the user to enter a number
    except:
        num2 = input("PLEASE ENTER A NUMBER:")

# the if-elif statement that calculates the total
if operator == "+":
    total = num1 + num2
elif operator == '-':
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/" and num2 > 0:
    total = num1 / num2
else:
    total = "ERROR"

print("the total is", total)
