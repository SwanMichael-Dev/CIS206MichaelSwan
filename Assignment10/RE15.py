import re

def remove_multiple_spaces(text):
    cleaned_text = re.sub(r'\s+', ' ', text)
    return cleaned_text.strip()

test_string = 'Python      Exercises'
result = remove_multiple_spaces(test_string)
print(result)
