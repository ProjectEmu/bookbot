def words(text):
    words = text.split()
    return len(words)
    
def character_count(text):
    text = text.lower()
    return {char: text.count(char) for char in set(text) if char.isalpha()}

def print_report(book_path):
    with open(book_path) as f:
        book = f.read()
    print(f"--- Begin report of {book_path} ---")
    print(f"{words(book)} words found in the document")
    for char, count in sorted(character_count(book).items(), key=lambda item: item[1], reverse=True):
        print(f"The '{char}' character was found {count} times")

def main():
    print_report("./books/frankenstein.txt")

    
main()