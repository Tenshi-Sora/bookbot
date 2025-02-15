with open("books/frankenstein.txt") as f: # returns the frankenstein book as a string
    file_contents = f.read()

file_contents_word_count = len(file_contents.split()) # splits the singular string by word then gives the length/count of them
print(file_contents_word_count)