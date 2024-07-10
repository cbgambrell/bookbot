def sort_on(dict):
    return dict['num']

def sort_dict(dict_sort):
    dict_array = []
    for k in dict_sort:
        temp_dict = {'char':k, 'num':dict_sort[k]}
        dict_array.append(temp_dict)
    dict_array.sort(reverse=True, key=sort_on)
    return dict_array

def char_count(book_text = ""):
    lower_text = book_text.lower()
    dict_of_char = {}
    for c in lower_text:
        if c.isalpha():
            if c not in dict_of_char.keys():
                dict_of_char[c] = 1
            else:
                dict_of_char[c] = dict_of_char[c] + 1
    sorted_list = sort_dict(dict_of_char)
    return sorted_list

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        words = file_contents.split()
        dict_of_char = char_count(file_contents)

        print("--- Begin report of books/frankenstein.txt ---\n")
        print(f"{len(words)} words found in the document\n")
        for k in dict_of_char:
            print(f"The {k['char']} character was found {k['num']} times.")
        print("--- End report ---")

main()

