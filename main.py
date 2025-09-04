from stats import count_words, character_count, sorted_dictionaries
import sys

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {sys.argv[1]}")
    print("----------- Word Count ----------")
    count_words(sys.argv[1])
    print("--------- Character Count -------")
    sorted_dictionaries(character_count(sys.argv[1]))
    print("============= END ===============")
main()