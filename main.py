import sys
from stats import count_words, count_characters, sort_characters

def get_book_text(book_path):
    with open(book_path, 'r', encoding='utf-8') as file:
        return file.read()

def main():
    if len(sys.argv) < 2:
        print("'Usage: python3 main.py <path_to_book>'")
        sys.exit(1)
    book_path = sys.argv[1]
    #print("============ BOOKBOT ============")
    #print(f"Analyzing book at: {book_path}")
    num_words = count_words(get_book_text(book_path))
    #print("----------- Word Count ----------")
    print(f"'Found {num_words} total words'")
    char_count = count_characters(get_book_text(book_path))
    #print("-------- Character Count --------")
    sorted_characters = sort_characters(char_count)
    for item in sorted_characters:
        if(item['char'].isalpha()):
            print(f"'{item['char']}: {item['num']}'")
    #print("============= END ===============")
    

main()