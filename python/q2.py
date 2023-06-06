def is_valid_string(s):
    # Count the frequency of each character
    char_count = {}
    for char in s:
        char_count[char] = char_count.get(char, 0) + 1

    # Count the frequency of each frequency
    freq_count = {}
    for count in char_count.values():
        freq_count[count] = freq_count.get(count, 0) + 1

    # If there is only one frequency or two frequencies with a difference of one,
    # the string is valid
    if len(freq_count) == 1 or (len(freq_count) == 2 and 1 in freq_count.values()):
        return "YES"
    else:
        return "NO"

print(is_valid_string("abc"))
print(is_valid_string("abcc"))