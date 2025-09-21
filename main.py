from stats import count_num_words, count_num_characters
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    num_char = {}
    book = get_book_text(path_to_file)
    num_words = count_num_words(book)
    num_char = count_num_characters(book)
    print(f"{num_words} words found in the document")
    print(num_char)


main("books/frankenstein.txt")