def get_book_text(filepath):
    contents = ""
    
    with open(filepath) as f:
        contents = f.read()
    
    return contents

def main():
    
    book_path = "books/frankenstein.txt"
    book_contents = get_book_text(book_path)
    print(book_contents)

main()