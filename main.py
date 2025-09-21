def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_contents = f.read()
    return file_contents

def count_num_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def main(path_to_file):
    book = get_book_text(path_to_file)
    num_words = count_num_words(book)
    print(f"{num_words} words found in the document")

main("books/frankenstein.txt")