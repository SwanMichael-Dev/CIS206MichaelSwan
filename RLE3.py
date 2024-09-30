def rle_encode(text):
  
  if not isinstance(text, str):
    raise TypeError("Input must be a string.")
  encoded_text = ""
  count = 1
  for i in range(1, len(text)):
    if text[i] == text[i - 1]:
      count += 1
    else:
      encoded_text += text[i - 1]
      if count > 1:
        encoded_text += str(count)
      count = 1
  encoded_text += text[-1]
  if count > 1:
    encoded_text += str(count)
  return encoded_text


def rle_decode(text):
  
  if not isinstance(text, str):
    raise TypeError("Input must be a string.")
  decoded_text = ""
  i = 0
  while i < len(text):
    char = text[i]
    if i + 1 < len(text) and text[i + 1].isdigit():
      if char == '#' and text[i + 1] == '#':
        decoded_text += '#'
        i += 2
      else:
        count = int(text[i + 1])
        decoded_text += char * count
        i += 2
    else:
      decoded_text += char
      i += 1
  return decoded_text


def main():
  
  while True:
    text = input("Enter a string (begin with ##00 for encoded): ")
    if text.startswith("##00"):
      try:
        decoded_text = rle_decode(text[4:])
        print(f"The decoded string is: {decoded_text}")
      except TypeError as e:
        print(e)
      except ValueError as e:
        print(e)
    else:
      try:
        encoded_text = rle_encode(text)
        print(f"The run-length encoded string is: {encoded_text}")
      except TypeError as e:
        print(e)
      except ValueError as e:
        print(e)


if __name__ == "__main__":
  main()