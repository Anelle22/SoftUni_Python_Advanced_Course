text = input()
dictionary = {}

for character in text:
    if character not in dictionary:
        dictionary[character] = 1
    else:
        dictionary[character] += 1

for key, value in sorted(dictionary.items()):
    print(f"{key}: {value} time/s")
