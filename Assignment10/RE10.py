import re

def replace_whitespace_and_underscore(text):
    temp = re.sub(r'_', '__TEMP__', text)
    temp = re.sub(r'\s+', '_', temp)
    cleaned_text = re.sub(r'__TEMP__', ' ', temp)
    return cleaned_text


text1 = "Regular Expressions"
text2 = "Code_Examples"

result1 = replace_whitespace_and_underscore(text1)
result2 = replace_whitespace_and_underscore(text2)

print(result1)  
print(result2)  
