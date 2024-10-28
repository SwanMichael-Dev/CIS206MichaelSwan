import re

def find_words_starting_with_a_or_e(text):
    pattern = r'\b[ae]\w*'
    matches = re.findall(pattern, text, re.IGNORECASE)
    return matches


text = (
    "The following example creates an ArrayList with a capacity of 50 elements. "
    "Four elements are then added to the ArrayList and the ArrayList is trimmed accordingly."
)

result = find_words_starting_with_a_or_e(text)
print(result)
