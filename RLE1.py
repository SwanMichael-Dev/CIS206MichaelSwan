def rle_encode(text):

  if not isinstance(text, str):
    raise TypeError("Input must be a string.")
  if not text.isalpha():
    raise ValueError("Input must contain only alphabetic characters.")
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


def main():
  
  while True:
    text = input("Enter a string of alphabetic characters: ")
    try:
      encoded_text = rle_encode(text)
      print(f"The run-length encoded string is: {encoded_text}")
      break
    except TypeError as e:
      print(e)
    except ValueError as e:
      print(e)


if __name__ == "__main__":
  main()