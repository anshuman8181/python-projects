start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

squares = [i**2 for i in range(start, end + 1)]

even_squares = [sq for sq in squares if sq % 2 == 0]
odd_squares = [sq for sq in squares if sq % 2 != 0]

# Output the results
print("All square values:", squares)
print("Even square values:", even_squares)
print("Odd square values:", odd_squares)
