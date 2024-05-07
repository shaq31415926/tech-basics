def add_numbers(num1, num2):
    total = num1 + num2
    print(f"The total is {total}")

    return total


number1 = int(input("What is your first number?"))
number2 = int(input("What is your second number?"))

total = add_numbers(number1, number2)
num3 = int(input("Add another number:"))
total2 = add_numbers(total, num3)
