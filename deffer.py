def find_symmetric_difference(set1, set2):
    return set1.symmetric_difference(set2)

set1 = {1, 2, 3, 4}
set2 = {3, 4, 5, 6}

result = find_symmetric_difference(set1, set2)
print("Symmetric Difference:", result)
