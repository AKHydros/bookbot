import sys
from stats import words_string, count_occurence

filepath = sys.argv[1]

print('============ BOOKBOT ============')
print('Analyzing book found...')
print('----------- Word Count ----------')
words_string(filepath)
print('--------- Character Count -------')
count_occurence(filepath)
print('============= END ===============')
