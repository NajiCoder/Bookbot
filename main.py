def main():
    path = "books/frankenstein.txt"
    text = get_text(path)
    word_count = get_words(text)
    letter_count_dict = count_letters(text)
    letter_sorted_list = letters_dict_to_sorted_list(letter_count_dict)
    print(f"--- Begin report of {path} ---")
    print()

    for letter in letter_sorted_list:
        print(f"the '{letter['letter']}' character was found {letter['num']} times.")

    print(f"--- End report of {path} ---")

def get_text(path):
    with open(path) as file:
        file_contents = file.read()
    return file_contents
    
def get_words(text):
    words = text.split()
    return len(words)

def count_letters(text):
    my_text = text.lower()
    letter_count = {}
    for letter in my_text:
        if letter.isalpha():
            if letter in letter_count:
                letter_count[letter] += 1
            else:
                letter_count[letter] = 1

    return letter_count


# turn the dicionary into a sorted list of dictionaries
def sort_on(dict):
    return dict["num"]


def letters_dict_to_sorted_list(letters_count_dict):
    sorted_list = []
    for letter in letters_count_dict:
        sorted_list.append({"letter": letter, "num": letters_count_dict[letter]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list


def print_letter_count(letter_count):
    for letter, count in letter_count.items():
        print(f"the '{letter}' character was found {count} times.")


if __name__ == "__main__":
    main()

    