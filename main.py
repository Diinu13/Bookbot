
import sys
from stats import get_num_words, get_chars_dict, count_characters

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        return f.read()

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    path = sys.argv[1]
    book = get_book_text(path)

        



    num_words = get_num_words(book)
    print(f"Found {num_words} total words")
    
    chars = get_chars_dict(book)
    sorted_chars = count_characters(chars)
    for item in sorted_chars:
        char = item["char"]
        num=item["num"]
        if char.isalpha():
            print(f"{char}: {num}")

    
main()