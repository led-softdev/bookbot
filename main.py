def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text):
    lowered = book_text.lower()
    char_counts = {}
    for char in lowered:
        if char not in char_counts:
            char_counts[char] = 1
        else:
            char_counts[char] += 1
    return char_counts

# A function that takes a dictionary and returns the value of the "num" key
# This is how the `.sort()` method knows how to sort the list of dictionaries
def sort_on(dict):
    return dict["count"]

def sorted_chars(char_counts):
    alpha_chars = [{"char":char, "count":count} for char, count in char_counts.items() if char.isalpha()]
    alpha_chars.sort(reverse=True,key=sort_on)
    return alpha_chars

def print_report(word_counts, sorted_chars, book_name):
    print(f"--- Begin report of {book_name} ---")
    print(f"There are {word_counts} words found in this book.\n")

    for dict in sorted_chars:
        print(f"The '{dict["char"]}' character was found {dict["count"]} times")
    
    print("\n--- End report ---")


book = "books/frankenstein.txt"
with open(book) as f:
    file_contents = f.read()

word_counts = count_words(file_contents)
sorted_chars = sorted_chars(count_chars(file_contents))
print_report(word_counts, sorted_chars, book)