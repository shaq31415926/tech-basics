def my_name_function(first_name, middle_name, last_name):
    if middle_name == "":
        print(f"Hi my name is {first_name} {last_name}")
    else:
        print(f"Hi my name is {first_name} {middle_name} {last_name}")


name1 = input("What is your first name?:")
name2 = input("What is your middle name?:")
name3 = input("What is your last name?:")

my_name_function(name1, name2, name3)
