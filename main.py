from stats import word_count, get_book_text, char_count, chars_dict_to_sorted_list
import sys

def print_report(book_path: str, word_count: int, sorted_list: list[tuple[str, int]]) -> None:
    print(f"============ BOOKBOT ============ \nAnalyzing book found at {book_path}... \n----------- Word Count ----------\nFound {word_count} total words")
    print("--------- Character Count -------")
    for c in sorted_list:
        if c[0].isalpha():
            print(f"{c[0]}: {c[1]}")
        else:
            continue
    print("============= END ===============")
def main():

    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    book_path = sys.argv[1]
    text = get_book_text(book_path)
    counts = char_count(text)

    print_report(book_path, word_count(text), chars_dict_to_sorted_list(counts))

main()
