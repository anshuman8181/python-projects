def multiply_list(numbers):
    product = 1
    for num in numbers:
        product *= num
    return product


my_list = [2, 3, 4, 5]
result = multiply_list(my_list)
print("Product of all numbers in the list:", result)
