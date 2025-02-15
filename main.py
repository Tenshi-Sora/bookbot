with open("books/frankenstein.txt") as f: # returns the frankenstein book as a string
    file_contents = f.read()

file_contents_word_count = len(file_contents.split()) # splits the singular string by word then gives the length/count of them
print(file_contents_word_count)

file_contents_letter_split = list(file_contents.lower()) # returns the letters and symbles split
file_contents_letter_count = {}
for x in file_contents_letter_split: # returns a dict of the letters as key and how freaquently they show up as a value
    if x in file_contents_letter_count:
        file_contents_letter_count[x] += 1
    else:
        file_contents_letter_count[x] = 1
file_contents_letter_count = dict(sorted(file_contents_letter_count.items(), key=lambda item: item[1], reverse=True)) # re-organizes them by highest count first
print(file_contents_letter_count)