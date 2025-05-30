test_dict = {
    'a': 10,
    'b': 20,
    'c': 10,
    'd': 30,
    'e': 20,
    'f': 10
}

frequency = {}

for value in test_dict.values():
    if value in frequency:
        frequency[value] += 1
    else:
        frequency[value] = 1

print("Frequency of values in dictionary:")
for key, val in frequency.items():
    print(str(key) + ": " + str(val))
