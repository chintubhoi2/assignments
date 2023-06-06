def highest_frequency_word_length(input_string):
    # Split the string into words
    words = input_string.split()

    # Count the frequency of each word
    word_frequency = Counter(words)

    # Find the highest frequency
    max_frequency = max(word_frequency.values())

    # Find the length of the highest-frequency word
    highest_frequency_word_length = max(len(word) for word, freq in word_frequency.items() if freq== max_frequency)

    return highest_frequency_word_length


# Test_case_1
str1 = "write write write all the number from from from"
res1 = find_highest_frequency_word_length(input_str1)
print("Length of the highest-frequency word in test case 1:", result1)

# Test_case_2
str2 = "hello hello world welcome welcome welcome to "
res2 = find_highest_frequency_word_length(str1)
print("Length of the highest-frequency word in test case 1:", result1)