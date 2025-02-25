from stats import get_num_words
import sys

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)

path = sys.argv[1]
with open(path) as f:
    file_contents = f.read()

file_contents_word_count = len(file_contents.split()) # splits the singular string by word then gives the length/count of them

file_contents_letter_split = list(file_contents.lower()) # returns the letters and symbles split
file_contents_letter_count = {}
for x in file_contents_letter_split: # returns a dict of the letters as key and how freaquently they show up as a value
    if x in file_contents_letter_count:
        file_contents_letter_count[x] += 1
    else:
        file_contents_letter_count[x] = 1
file_contents_letter_count = dict(sorted(file_contents_letter_count.items(), key=lambda item: item[1], reverse=True)) # re-organizes them by highest count first

file_contents_just_letters = {}
for x, y in file_contents_letter_count.items(): # returns only letters
    if x.isalpha():
        file_contents_just_letters[x] = y
file_contents_just_letters = dict(sorted(file_contents_just_letters.items(), key=lambda item: item[0])) # re-organizes in alphabetical order by key
def text_print_loop(x, y): # loop for bottom text to print properly
    return f"{x}: {y}"  # Return a string instead of printing
print(f"""
--- Begin report of books/frankenstein.txt ---
{file_contents_word_count} words found in the document

{"\n".join(text_print_loop(x, y) for x, y in file_contents_just_letters.items())}
--- End report ---
""")