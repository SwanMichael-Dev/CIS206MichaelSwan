import re

def check_string(string):
    pattern = r"^[a-zA-Z0-9]*$"
    if re.match(pattern, string):
        return True
    else:
        return False
if __name__ == "__main__":
    test_string1 = "ABCDEFabcdef123450"
    test_string2 = "*&%@#!}{"
    print(f"Test string 1: {test_string1}, result: {check_string(test_string1)}")
    print(f"Test string 2: {test_string2}, result: {check_string(test_string2)}")
