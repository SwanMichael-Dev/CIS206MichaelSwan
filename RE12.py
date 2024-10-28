def find_words_starting_with_a_or_e(text):
    words = text.split()
    result = [word for word in words if word.lower().startswith(('a', 'e'))]
    return result


string = "The following example creates an ArrayList with a capacity of 50 elements. Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
words_found = find_words_starting_with_a_or_e(string)
print(f"Words starting with 'a' or 'e': {words_found}")