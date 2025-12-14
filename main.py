import sys
from stats import count_words, count_characters, sort_list_of_dictionaries


def get_book_text(filepath):
    contents = ""
    
    with open(filepath) as f:
        contents = f.read()
    
    return contents


def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    book_path = sys.argv[1]
    print(f"Analyzing book found at {book_path}...")
    book_contents = get_book_text(book_path)
    word_count = count_words(book_contents)
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    character_count_dictionary = count_characters(book_contents)
    list_of_characters = sort_list_of_dictionaries(character_count_dictionary)
    print("--------- Character Count -------")
    for entry in list_of_characters:
        if entry["char"].isalpha():
            print(f"{entry["char"]}: {entry["num"]}")

main()