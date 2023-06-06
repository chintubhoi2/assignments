def find_frequent_string_length(sent):
  word_count = dict()
  #frequent_words = []

  #storing distinct word frequency into a dictionary
  for word in sent.split():
    if word in word_count.keys():
      word_count[word] += 1
    else:
      word_count[word] = 1
  #sorting the dictionary based on frequency of words
  word_count = sorted(word_count.items(),key = lambda x:x[1],reverse=True)
  #storing maximum occuring word frequency
  max_count = word_count[0][1]
  max_length=0 #for checking length of each word
  for key,item in word_count:
    if item == max_count:
      if len(key) > max_length:
        max_length = len(key)
    else:
      break
  return max_length
  #print(word_count)


# Test_case_1
str1 = "write write write all the number from from from"
res1 = find_frequent_string_length(str1)
print("Length of the highest-frequency word in test case 1:", res1)

# Test_case_2
str2 = "hello hello world welcome welcome welcome to "
res2 = find_frequent_string_length(str2)
print("Length of the highest-frequency word in test case 1:", res2)
