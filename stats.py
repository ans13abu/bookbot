def count_words(book_text):
    words = book_text.split()
    return len(words)

def count_characters(book_text):
    char_count = {}
    for char in book_text:
        if char.lower() in char_count:
            char_count[char.lower()] += 1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(items):
    return items["num"]

def sort_characters(dictionary):
    sorted_list = []
    for item in dictionary.items():
        dict = {}
        dict['char'] = item[0]
        dict['num'] = item[1]
        sorted_list.append(dict)

    sorted_list.sort(key=sort_on,  reverse=True)
    return sorted_list