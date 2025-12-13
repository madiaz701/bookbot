def get_book_text(filepath):
    contents = ""
    
    with open(filepath) as f:
        contents = f.read()
    
    return contents

def count_words(text):
    list_of_words = text.split()
    counter = 0
    for word in list_of_words:
        counter += 1
    return counter


def main():
    
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    word_count = count_words(book_contents)
    print(f"Found {word_count} total words")

main()