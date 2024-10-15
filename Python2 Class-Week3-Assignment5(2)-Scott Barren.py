# Python 2 Class - Week 3 - Assignment 5 - Second method
# Scott Barren
#
# Description:
# Implement a recursive function to calculate the factorial of a non-negative integer.
# Instructions:
# Write a recursive function  factorial(n) that returns the factorial of the non-negative integer  n.
# The factorial of  n (denoted as  n!) is defined as:
# n! = n * (n-1)! for n > 0
# 0! = 1
# Write test cases to verify the function works correctly for different values of  n.
#
def factorial(n):
    #  Base Case to calculate the factorials
    if n == 0:
        return 1
    #  Recursive Case
    else:
        return n * factorial(n - 1)
def test():
    test_cases = [
        (0, 1),  # 0! = 1
        (1, 1),  # 1! = 1
        (2, 2),  # 2! = 2
        (3, 6),  # 3! = 6
        (4, 24),  # 4! = 24
        (5, 120),  # 5! = 120
        (6, 720),  # 6! = 720
        (7, 5040),  # 7! = 5040
        (10, 3628800),  # 10! = 3628800
    ]
    for n, expected in test_cases:
        result = factorial(n)
        print(f"factorial({n}) = {result}, expected = {expected}")
        if result == expected:
            print("TEST PASSED!")
        else:
            print("TEST FAILED!!!!")

test()