num1 = input("Select first number:")

# loop through the try and except so the user can not select an operator
# until they have entered a number

while True:
    try:
        # check if num1 can be converted to a float
        # if so, ask the user for operator
        num1 = float(num1)
        break
    except:
        # if the user does not enter a number, ask for input again
        num1 = input("Please only input numbers:")

# validation for operator
operator = input("Please select an operator [+, -, *, /]:")
while operator not in ['+', '-', '*', '/']:
    operator = input("Please select ONLY the following [+, -, *, /]:")

# validation for second number
num2 = input("Select second number:")
while True:
    try:
        num2 = float(num2)
        break
    except:
        num2 = input("Please only input numbers:")

# the if-else-if logic that calculates the total, as covered in class # 2
if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/" and num2 > 0:
    total = num1 / num2
else:
    total = "ERROR"

# print("The answer is", total)
print(f"The answer is {total}")