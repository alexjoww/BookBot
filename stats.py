def get_book_text(file_path: str) -> str:
    with open(file_path) as f:
        file_contents = f.read()
    return file_contents

def word_count(text: str) -> int:
    words = text.split()

    return len(words)

def char_count(text: str) -> dict[str, int]:
    lowercase_text = text.lower()
    counts = {}

    for char in lowercase_text:
        if char in counts:
            counts[char] += 1
        else:
            counts[char] = 1
    return counts

def sort_on(char: tuple[str, int]) -> int:
    return char[1]

def chars_dict_to_sorted_list(counts: dict[str, int]) -> list[tuple[str, int]]:
    new_list = []

    for c in counts:
        new_list.append((c, counts[c]))

    sorted_list = sorted(new_list, reverse=True, key=sort_on)

    return sorted_list
