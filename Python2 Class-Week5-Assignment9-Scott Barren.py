# Python 2 Class - Week 5 - Assignment 9
# Scott Barren
#
# Explain the Merge Sort algorithm and demonstrate its implementation in Python to sort a list of strings in alphabetical order.
# Give an example
#
#
def merge_sort(list1):

    # If the list has 1 or 0 elements then it is already sorted
    if len (list1) <= 1:
        return list1

    # Find the middle point of Division for the list into Two seperate Halfs
    mid = len(list1) // 2

    # Sort Both Halves Recursively
    left1 = merge_sort(list1[:mid])  # Sort the left half
    right1 = merge_sort(list1[mid:])  # Sort the right half

    # Merge the Sorted Halves
    return merge(left1, right1)

def merge(left, right):

    merged = []  # This holds the merged results
    i = j = 0  # Pointers for the left and right lists

    # Compare the elements from both lists and begin adding the smaller one to the merged list

    while i < len(left) and j < len(right):
        if left[i] < right[j]:
            merged.append(left[i])  # Adding the smallest element in the list from the left
            i += 1 # This will move my pointers in the left direction
        else:
            merged.append(right[j])  # Adding smaller Element from the RIGHT
            j += 1  # Move Pointer in the Right Direction

    # If there are REMAINING elements in the LEFT List then ADD them
    while i < len(left):
        merged.append(left[i])
        i += 1

    # If there are REMAINING elements in the RIGHT List then ADD them
    while j < len(right):
        merged.append(right[j])
        j += 1

    return merged # This will return the MERGED SORTED LIST

strings = ["salmon", "tuna", "bass", "trout", "halibut", "shrimp", "crab", "cod", "swordfish", "clams"]

print("Original List: ", strings)

sortedlist = merge_sort(strings)

print("Sorted List: ", sortedlist)