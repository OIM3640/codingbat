def missing_char(word, num):
    final_word = word.replace(word[num],"")
    print(final_word)

missing_char('kitten', 1)
missing_char('kitten', 0)
missing_char('kitten', 4)