def word_count(text):
    return len(text.split())

def letter_count(text):
    letters = {}

    for letter in text:
        l = letter.lower()
        if l in letters:
            letters[l] += 1
        else:
            letters[l] = 1
    return letters

with open("books/frankenstein.txt") as f:
    file_content = f.read()
    print(letter_count(file_content))


