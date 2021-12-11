def string_splosion(word):
    num = len(word) 
    final_word = ""
    for i in range(num):
        final_word = final_word + word[:i+1]
    print (final_word)

string_splosion('Code')
string_splosion('abc')
string_splosion('ab')      