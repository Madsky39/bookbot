from stats import count_num_words, count_num_characters, sort_dicts
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
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
        
    


main("books/frankenstein.txt")