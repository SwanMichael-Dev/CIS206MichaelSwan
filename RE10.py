def replace_chars(text):
    result = ""
    for char in text:
        if char == " ":
            result += "_"
        elif char == "_":
            result += " "
        else:
            result += char
    return result

print("Testing with 'Regular Expressions':", replace_chars("Regular Expressions"))
print("Testing with 'Code_Examples':", replace_chars("Code_Examples"))
text = input("Enter a string: ")
new_text = replace_chars(text)
print("The new string is:", new_text)