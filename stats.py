import sys

# Counting the number of words in a document

def get_book_text(filepath):
    with open(filepath) as f:
        file_contents = f.read()
        return file_contents

def words_string(filepath):
    books_text = get_book_text(filepath) #remove
    words = books_text.split()
    print (f'Found {len(words)} total words')

def count_occurence(filepath):
    books_text = get_book_text(filepath)
    characters = {}

#conversion to lowe case to count
    books_text = books_text.lower()

#counter function
    for char in books_text:
        if char.isalpha():
            characters[char] = characters.get(char,0) + 1

#print results
    for char, count in sorted(characters.items(), key= lambda x: x[1], reverse=True):
        print(f"{char}: {count}")

#checking arguments and running

if len(sys.argv) < 2:
    print(' Usage: python3 main.py <path_to_book>')
    sys.exit(1)

