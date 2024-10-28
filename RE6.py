import re

def find_z_word(text):
  match = re.search(r'\b\w*z\w*\b', text)
  if match:
    return match.group(0)
  else:
    return None


text1 = "The quick brown fox jumps over the lazy dog."
text2 = "Python Exercises."

print(find_z_word(text1))
print(find_z_word(text2))  