f = open("names.txt", "r")
names = f.read().splitlines()
f.close()
while True:
    name = input("Enter a name: ")  
    if name in names:
        print(f"The string '{name}' is already in the file.")  
    else:
      print(f"The string '{name}' has been written to output.txt")