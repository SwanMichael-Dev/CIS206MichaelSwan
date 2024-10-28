def replace_chars(text):
    return text.replace(" ", ":").replace(",", ":").replace(".", ":")
if __name__ == "__main__":
    text = 'Python Exercises, PHP exercises.'
    print(replace_chars(text))