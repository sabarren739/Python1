# Python 2 Class - Week 5 - Assignment 7
# Scott Barren
#
# How would you implement the Bubble Sort algorithm in Python to sort a list of numbers in ascending order?
# Give an exmaple
#
#
# Define Function and logic for sort
def bubble_sort(numbers):
    n = len(numbers)
    # Traverse through all list elements
    for i in range(n):
        # The last i elements are already sorted and do not need to be checked
        for j in range(0, n-i-1):
            # Swap the numbers if the number found is greater than the next number
            if numbers[j] > numbers[j+1]:
                numbers[j], numbers[j+1] = numbers[j+1], numbers[j]

# Enter data and display results
numbers = [95, 65, 75, 55, 45, 15, 5]
print("Original list:", numbers)

bubble_sort(numbers)
print("Bubble-Sorted list:", numbers)