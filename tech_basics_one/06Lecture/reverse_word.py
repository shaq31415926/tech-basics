# ask the user for a word
text = input("Please enter a word:")


def word_count_of_text(text):
    """This function will count the length of the word"""

    character_count = len(text)

    return character_count


def reverse_string(text):
    """This function will do the following:
    - Count the length of the word
    - If the length is a multiple of four then it will print the reverse of the word, otherwise it will print the world"""

    # count the number of words in the text
    length = word_count_of_text(text)
    print(f"The number of the words is {length}")

    # if the remainder is zero when you divide by four then reverse the text
    if length % 4 == 0:
        print("This is a multiple of 4")
        print(text[::-1])
    else:
        print("This is not a multiple of 4")
        print(text)

# dont forget to call the definition
reverse_string(text)