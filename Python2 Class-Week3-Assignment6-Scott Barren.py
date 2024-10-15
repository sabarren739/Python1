# Python 2 Class - Week 3 - Assignment 6
# Scott Barren
#
# Implement a recursive function to compute the nth Fibonacci number.
# Instructions:
# Write a recursive function  fibonacci(n) that returns the nth Fibonacci number.
# The Fibonacci sequence is defined as:
# F(0) = 0
# F(1) = 1
# F(n) = F(n-1) + F(n-2) for n > 1
# Write test cases to verify the function works correctly for different values of  n.
#
#
# Implementing the recursive function to compute the nth Fibonacci number
def fibonacci(n):  # Base cases: F(0) = 0 and F(1) = 1
    if n == 0:
        return 0
    elif n == 1:
        return 1
    # Recursive case: F(n) = F(n-1) + F(n-2)
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

# Test cases to verify the function works correctly for different values of n
test_cases = [0, 1, 5, 10, 15, 30]
fibonacci_results = {n: fibonacci(n) for n in test_cases}

# Display the results
print("The Fibonacci results of Test Case Numbers: ", test_cases, " are ", fibonacci_results)