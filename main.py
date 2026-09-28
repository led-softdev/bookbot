import sys
from stats import count_words, count_chars, chars_dict_to_sorted_list

def print_report(book, word_counts, sorted_chars):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book}...")
    print("----------- Word Count ----------")
    print(f"Found {word_counts} total words")
    print("--------- Character Count -------")

    for tuple in sorted_chars:
        print(f"{tuple[0]}: {tuple[1]}")
    
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

book = sys.argv[1]
with open(book) as f:
    file_contents = f.read()

word_counts = count_words(file_contents)
char_counts = count_chars(file_contents)
sorted_chars = chars_dict_to_sorted_list(char_counts)
print_report(book, word_counts, sorted_chars)