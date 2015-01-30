
# Occurrences of a specified character in a string

def count_letter(str, ch):
    a = []
    for letter in str:
        a.append(letter)
    return a.count(ch)

print(count_letter("Welcome", "e"))

