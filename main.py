def sorting(dict):
    return dict["count"]

def character_list(text):
    char_list = []
    for characters in text:
        if characters.isalpha() == True:
            new_dict = {}
            new_dict['char'] = characters
            new_dict['count'] = text[characters]
            char_list.append(new_dict)
    char_list.sort(reverse=True, key=sorting)
    return char_list

def count_characters(char):
    charl = char.lower()
    char_count = {}
    for words in charl:
        if words in char_count:
            char_count[words] += 1
        else:
            char_count[words] = 1
    return char_count
        
    
def count_words(text):
    words = text.split()
    return len(words)

def main():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
        word_count = count_words(file_contents)
        character_count = count_characters(file_contents)
        char_list = character_list(character_count)
        print("---Begin report of books/frankenstein.txt---")
        print(f"{word_count} words found in the document")
        for characters in char_list:
            number = characters['count']
            char = characters['char']
            print(f"The '{char}' character was found {number} times")
        print("--- End Report ---")
main()



    