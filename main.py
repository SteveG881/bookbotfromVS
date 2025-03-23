from stats import word_count
from stats import char_counts
from stats import sort_by_count
import sys

def get_book_text(path):
    with open(path) as book:
        contents = book.read()
    return contents

def main():
    #path = "~/dev_files/bookbot/books/frankenstein.txt"
    #path_to_book = "./books/frankenstein.txt"
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    path_to_book = sys.argv[1]

    count = word_count(get_book_text(path_to_book))

    char_dictionary = char_counts(get_book_text(path_to_book))

    sorted_dictionary = sort_by_count(char_dictionary)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {path_to_book}...")
    print("----------- Word Count ----------")
    print(f"Found {count} total words")
    print("--------- Character Count -------")
    for key, value in sorted_dictionary.items():
        if key.isalpha():
            print(f"{key}: {value}")

    print("============= END ===============")

main()