import re

def match_word_at_beginning(text):
  match = re.match(r"\b\w+", text)
  if match:
    return match.group(0)
  else:
    return None


text1 = "The quick brown fox jumps over the lazy dog."
text2 = " The quick brown fox jumps over the lazy dog."

print(f"Text: '{text1}' - Matched word: '{match_word_at_beginning(text1)}'")
print(f"Text: '{text2}' - Matched word: '{match_word_at_beginning(text2)}'")
