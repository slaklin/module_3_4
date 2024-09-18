def single_root_words(root_word, *other_words):
    same_words = []
    new_root_word = root_word.lower()
    new_other_words = []
    for i in other_words:
        new_other_words.append(i.lower())
    for j in new_other_words:
        if j in new_root_word or new_root_word in j:
            same_words.append(j)
    return same_words


print(single_root_words('rich', 'richiest', 'orichalcum', 'cheers', 'richies'))
print(single_root_words('Disablement', 'Able', 'Mable', 'Disable', 'Bagel'))
