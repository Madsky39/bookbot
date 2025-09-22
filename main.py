from stats import count_num_words, count_num_characters, sort_dicts
import sys

def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    num_char = {}
    book = get_book_text(path_to_file)
    num_words = count_num_words(book)
    num_char = count_num_characters(book)
    sorted_list = sort_dicts(num_char)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        
    

if len(sys.argv) < 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
main(sys.argv[1])