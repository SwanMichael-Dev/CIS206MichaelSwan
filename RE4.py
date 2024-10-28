import re

def find_sequences(text):
    return re.findall(r'[a-z]+_[a-z]+', text)

test_cases = [
    "aab_cbbbc",
    "aab_Abbbc",
    "Aaab_abbbc"
]

for text in test_cases:
    sequences = find_sequences(text)
    print(f"Sequences in '{text}': {sequences}")