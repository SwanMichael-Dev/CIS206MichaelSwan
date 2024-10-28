def find_words_starting_with_a_or_e(text):
    words = text.split()
    result = []
    for word in words:
        if word.lower().startswith(('a', 'e')):
            result.append(word)
    return result


text = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
words = find_words_starting_with_a_or_e(text)
print(f"Words starting with 'a' or 'e': {words}")