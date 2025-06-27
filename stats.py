# Counting the number of words in a document

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def words_string():
    books_text = get_book_text('books/frankenstein.txt')
    words = books_text.split()
    print (f'{len(words)} words found in the document')

