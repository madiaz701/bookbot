from stats import count_words, count_characters

def get_book_text(filepath):
    contents = ""
    
    with open(filepath) as f:
        contents = f.read()
    
    return contents


def main():
    
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    word_count = count_words(book_contents)
    print(f"Found {word_count} total words")
    character_count_dictionary = count_characters(book_contents)
    print(character_count_dictionary)

main()