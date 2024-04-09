# creating input statements to ask user for numbers and operators
num1 = input("Please select the first number:")
operator = input("Please select an operator (+, -, *, /):")
num2 = input("Please select the second number:")

# converting the numbers to be floats, otherwise they default to style
num1 = float(num1)
num2 = float(num2)

print("The calculation is:", num1, operator, num2)

# the if-elif statement
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

# print("The total is", total)
print(f"The total is {total}")
