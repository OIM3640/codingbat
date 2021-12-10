def front_back(word):
    word = list(word)
    word = word[0]
    word1 = word[-1]
    final_word = word.replace(word[0], word[-1])
    final2_word = final_word.join(word1)
    print (final_word)

front_back('code')
front_back('a')
front_back('ab')