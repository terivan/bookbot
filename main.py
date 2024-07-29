from copy import copy

with open('books/frankenstein.txt') as f:
    file_contents = f.read()
    words = file_contents.split()


def count_letters(text_file):
    out_dict = {}
    dt = copy(text_file).lower()
    for i in dt:
        if i in out_dict:
            out_dict[i] += 1
        else:
            out_dict[i] = 1
    return out_dict

a = (count_letters(file_contents))
b = ((list(sorted(a.items(), key=lambda item: item[1]))))

print("""--- Begin report of books/frankenstein.txt ---""")
print("""\n""")
print(f"""{len(words)} words found in the document""")
print("""\n""")
for i in reversed(b):
    if i[0].isalpha()==True:
        print(f"""The {i[0]} character was found {i[1]} times
            """)
    else:
        continue

print("""\n""")
print("""--- End report ---""")