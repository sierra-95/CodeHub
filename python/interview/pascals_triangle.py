#!/usr/bin/env python3
def pascals_expansion(n):
    coefficients = [1]  # Start with the initial [1]
    for i in range(1, n + 1):
        next_coefficients = [1]  # Each row starts and ends with 1
        for j in range(1, i):
            next_coefficients.append(coefficients[j - 1] + coefficients[j])
        next_coefficients.append(1)
        coefficients = next_coefficients
    return coefficients

# Example: Get the coefficients for (x + y)^3
result = pascals_expansion(4)
print(result)  # Output: [1, 3, 3, 1]



#Create a function def pascal_triangle(n): that returns a list of lists of integers representing the Pascal’s triangle of n:
#Returns an empty list if n <= 0
#You can assume n will be always an integer
#    [1]        (x+y)^0     x=1 y=1
#   [1,1]   
#  [1,2,1]      (x+y)^0 =   x(squared)+ 2xy + y(squared)= 1+2+1
# [1,3,3,1]
#[1,4,6,4,1]
#pascals- Each new number lies between two numbers and below them,
#and its value is the sum of the two numbers above it.
