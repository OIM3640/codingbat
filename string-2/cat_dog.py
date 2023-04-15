def cat_dog(str):
    """
    Return True if the string "cat" and "dog" appear the same number of times in the given string.
    """
    cat_count, dog_count = 0, 0
    for i in range(len(str)-2):
        if "cat" in str[i:i+3]:
            cat_count += 1
        elif "dog" in str[i:i+3]:
            dog_count += 1
    return cat_count == dog_count

print(cat_dog('catdog'))
print(cat_dog('catcat'))
print(cat_dog('1cat1cadodog'))