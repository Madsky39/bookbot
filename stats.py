def count_num_words(book):
    words = book.split()
    count = 0
    for word in words:
        count += 1
    return count

def count_num_characters(book):
    book_dict = {}
    for char in book:
        if char.lower() in book_dict:
            book_dict[char.lower()] += 1
            continue
        else:
            book_dict[char.lower()] = 1
    return book_dict