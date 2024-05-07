shape = input("What shape would you like to calculate the area of?")


def calc_square_area(length):
    area = length ** 2

    print(f"The area is {area} cm2")
    return area


def calc_rectangle_area(height, width):
    area = height * width

    print(f"The area is {area} cm2")
    return area


if shape == "square":
    length = int(input("What is the length of the square cm?"))
    calc_square_area(length)
elif shape == "rectangle":
    height = int(input("What is the height of the rectangle cm?"))
    width = int(input("What is the width of the rectangle cm?"))
    calc_rectangle_area(height, width)
else:
    print("I AM NOT ABLE TO DO THIS RIGHT NOW")