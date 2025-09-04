def count_words(file_path):
    with open(file_path) as f:
        file_contents = f.read()
        words = file_contents.split()
        print(f"Found {len(words)} total words")

def character_count(file_path):
    letters = {
        "a": 0,
        "b": 0,
        "c": 0,
        "d": 0,
        "e": 0,
        "f": 0,
        "g": 0,
        "h": 0,
        "i": 0,
        "j": 0,
        "k": 0,
        "l": 0,
        "m": 0,
        "n": 0,
        "o": 0,
        "p": 0,
        "q": 0,
        "r": 0,
        "s": 0,
        "t": 0,
        "u": 0,
        "v": 0,
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0,
    }

    with open(file_path) as f:
        file_contents = f.read()
        for letter in file_contents:
            if letter.lower() in letters:
                letters[letter.lower()] += 1
                
    return letters

def sorted_dictionaries(dictionary):
    result = []
    for key, value in dictionary.items():
        result.append((key, value))
    result.sort(key=sort_on, reverse=True)
    for item in result:
        print(f"{item[0]}: {item[1]}")
    return result


def sort_on(items):
    return items[1]