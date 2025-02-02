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
        print(character_count)
main()



    