from stats import count_num_words
def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def main(path_to_file):
    book = get_book_text(path_to_file)
    num_words = count_num_words(book)
    print(f"{num_words} words found in the document")

main("books/frankenstein.txt")