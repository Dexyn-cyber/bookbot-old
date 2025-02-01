def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    chars_dict = get_chars_dict(text)


    print(" --- Begin report of books/frankenstein.txt ---")
    print(F"{num_words} words found in the document")
    for key, value in chars_dict.items():
        if isinstance(key, str) and key.isalpha():
            print(f"The '{key}' character was found {value} times")
    print("--- End Report ---")


def get_num_words(text):
    words = text.split()
    return len(words)


def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars


def get_book_text(path):
    with open(path) as f:
        return f.read()


main()
