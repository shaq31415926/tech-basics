# These definitions have been generated with the help of ChatGPT
def calculate_life_path_number(dob):
    def reduce_to_single_digit(num):
        while num > 9 and num not in [11, 22, 33]:
            num = sum(int(digit) for digit in str(num))
        return num

    # Extract day, month, and year
    year = dob.year
    month = dob.month
    day = dob.day

    # Sum all digits of the date
    total_sum = sum(int(digit) for digit in f"{year}{month}{day}")

    # Reduce to a single digit or master number
    return reduce_to_single_digit(total_sum)