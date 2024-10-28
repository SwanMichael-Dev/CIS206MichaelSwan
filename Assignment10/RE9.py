import re

def find_pattern(text, pattern):
 
    match = re.search(pattern, text)
    if match:
        return match.start(), match.end()
    else:
        return None

# Example usage
text = "The quick brown fox jumps over the lazy dog."
pattern = "fox"

result = find_pattern(text, pattern)

if result:
    print(f"Pattern '{pattern}' found at indices {result}")
else:
    print(f"Pattern '{pattern}' not found in the text.")
