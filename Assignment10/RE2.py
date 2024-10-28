import re

def match_string(text):
    pattern = r"ab*"
    match = re.match(pattern, text)
    if match:
        return True
    else:
        return False
if __name__ == "__main__":
    print(match_string("ab"))
    print(match_string("abc"))
    print(match_string("a"))
    print(match_string("ab"))
    print(match_string("abb"))
