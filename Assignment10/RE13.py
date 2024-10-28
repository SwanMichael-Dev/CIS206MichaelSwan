import re

def replace_characters(text):
    modified_text = re.sub(r'[ ,.]', ':', text)
    return modified_text


test_string = 'Python Exercises, PHP exercises.'
result = replace_characters(test_string)
print(result)

