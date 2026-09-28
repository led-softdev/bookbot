def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_chars(book_text) -> dict[str, int]:
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
def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(char_counts: dict[str, int]) -> list[tuple[str, int]]:
    sorted_alpha_chars_tuple_list = sorted([(char, count) for char, count in char_counts.items() if char.isalpha()], reverse=True, key=sort_on)
    return sorted_alpha_chars_tuple_list