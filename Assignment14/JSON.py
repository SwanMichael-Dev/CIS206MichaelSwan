import json

with open('library.json', 'r') as f:
    data = json.load(f)

while True:
    title = input("Enter a book title (or 'quit' to exit): ")
    if title.lower() == 'quit':
        break

    found = False
    for book in data['books']:
        if book['title'] == title:
            print(f"Title: {book['title']}")
            print(f"Author: {book['author']}")
            print(f"Year: {book['year']}")
            found = True
            break
    if not found:
        print(f"Title '{title}' not found in the library.")