def get_num_words():
    with open("books/frankenstein.txt") as f:
        file_contents = f.read()
    print(f"{len(file_contents.split())} words found in the document")