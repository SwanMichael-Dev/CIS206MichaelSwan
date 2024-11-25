import xml.etree.ElementTree as ET


tree = ET.parse('library.xml')
root = tree.getroot()

while True:
    title = input("Enter a book title (or 'quit' to exit): ")
    if title.lower() == 'quit':
        break

    found = False
    for book in root.findall('books/book'):
        if book.find('title').text == title:
            print(f"Title: {book.find('title').text}")
            print(f"Author: {book.find('author').text}")
            print(f"Year: {book.find('year').text}")
            found = True
            break
    if not found:
        print(f"Title '{title}' not found in the library.")