import re

def search_strings(text, search_terms):
    found_terms = {}
    for term in search_terms:
        # Use re.search to find the term in the text
        found_terms[term] = re.search(re.escape(term), text) is not None
    return found_terms


text = 'The quick brown fox jumps over the lazy dog.'


search_terms = ['fox', 'dog', 'horse']


results = search_strings(text, search_terms)


for term, found in results.items():
    if found:
        print(f"'{term}' was found in the text.")
    else:
        print(f"'{term}' was not found in the text.")
