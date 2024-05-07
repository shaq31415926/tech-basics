# ask the user for a word
text = input("Please enter a word or some text:")


def word_count_of_text(text):
    """This function will count the length of the word"""

    character_count = len(text)

    return character_count


word_count = word_count_of_text(text)
print(f"Your text contains {word_count} characters")