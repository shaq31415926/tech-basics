def calc_area(length):
    area = length ** 2

    return area


# this is a silly use case
# just wanted to showcase how you can return multiple outputs
def calc_area_and_volume(length):
    area = length ** 2
    volume = length ** 3

    return area, volume


length = int(input("What is the length in cm?:"))
area, volume = calc_area_and_volume(length)
print(f"The area of square is {area} cm2")
print(f"The volume of the cube is {volume} cm2")

# area, volume = calc_area_and_volume(area)
