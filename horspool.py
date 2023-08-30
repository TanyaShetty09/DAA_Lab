def shift_table(pattern):
    table = {}
    length = len(pattern)
    for i in range(length - 1):
        table[pattern[i]] = length - 1 - i
    return table

def horspool_search(text, pattern):
    n = len(text)
    m = len(pattern)
    table = shift_table(pattern)
    i = m - 1

    while i < n:
        k = 0
        while k < m and pattern[m - 1 - k] == text[i - k]:
            k += 1
        if k == m:
            return i - m + 1
        else:
            shift = table.get(text[i], m)
            i += shift

    return -1

text = input("Enter the text: ")
pattern = input("Enter the pattern to search: ")

position = horspool_search(text, pattern)
if position != -1:
    print(f"Pattern found at position {position}")
else:
    print("Pattern not found in the text")


'''Output:
Enter the text: algorithmisfun
Enter the pattern to search: fun
Pattern found at position 11
'''