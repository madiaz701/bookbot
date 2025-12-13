def count_words(text):
    list_of_words = text.split()
    counter = 0
    for word in list_of_words:
        counter += 1
    return counter

def count_characters(text):
    character_count_dictionary = {}
    for ch in text:
        lower_ch = ch.lower()
        if lower_ch not in character_count_dictionary:
            character_count_dictionary[lower_ch] = 1
        else:
            character_count_dictionary[lower_ch] += 1
    return character_count_dictionary
