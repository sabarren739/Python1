# Python 2 Class - Week 3 - Assignment 5 - First method
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
        assert factorial(0) == 1
        assert factorial(1) == 1
        assert factorial(2) == 2
        assert factorial(3) == 6
        assert factorial(4) == 24
        assert factorial(5) == 120
        assert factorial(10) == 3628800

        print("All Test Cases PASSED !!!!")

test()