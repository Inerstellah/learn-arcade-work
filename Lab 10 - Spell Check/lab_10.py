import re

# This function takes in a line of text and returns
# a list of words in the line.
def split_line(line):
    return re.findall('[A-Za-z]+(?:\'[A-Za-z]+)?',line)

def read_in_file(file_name):
    """ Read in lines from a file """

    # Open the file for reading, and store a pointer to it in the new
    # variable "file"
    my_file = open(file_name)

    # Create an empty list to store our names
    dictionary_list = []

    # Loop through each line in the file like a list
    for line in my_file:
        # Remove any line feed, carriage returns or spaces at the end of the line
        line = line.strip()

        # Add the name to the list
        dictionary_list.append(line)

    my_file.close()

    return dictionary_list

def linear_search(word, dictionary_list):
    """ Linear search """

    # Start at the beginning of the list
    current_word_position = 0

    # Loop until you reach the end of the dictionary, or the value at the
    # current position is equal to the word
    while current_word_position < len(dictionary_list) and dictionary_list[current_word_position] != word:

        # Advance to the next item in the list
        current_word_position += 1
    if current_word_position == len(dictionary_list):
        print(f"Possible misspelling: '{word}'")
        return True
    else:
        return False

def binary_search(word, dictionary_list):
    """ Binary search """

    lower_bound = 0
    upper_bound = len(dictionary_list) - 1

    while lower_bound <= upper_bound:
        middle_pos = (lower_bound + upper_bound) // 2
        middle_word = dictionary_list[middle_pos]

        if middle_word < word:
            lower_bound = middle_pos + 1
        elif middle_word > word:
            upper_bound = middle_pos - 1
        else:
            return True  # Word found

    print(f"Possible misspelling: '{word}'")
    return False

def main():

    dictionary_words = read_in_file("dictionary.txt")
    dictionary_words.sort()
    print(f"There are {len(dictionary_words)} words in the dictionary."
          f" Of these words, these are not included:\n")
    print("--- Linear Search ---")
    chapter_lines = read_in_file("AliceInWonderLand200.txt")
    chapter_words = []
    for line in chapter_lines:
        words = split_line(line)
        for word in words:
            chapter_words.append(word)
            word = word.upper()
            linear_search(word, dictionary_words)


main()