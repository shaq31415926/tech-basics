# create the input statements, where you can ask the user to select a number and operator
num1 = input("Please select the first number:")
operator = input("Please select your operator (+, -, *, /):")
num2 = input("Please select the second number:")

print(num1, operator, num2)

# fix the data type, otherwise it will be picked up as a string
num1 = float(num1)
num2 = float(num2)

# the if-elif-else statement where we calculate the result
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