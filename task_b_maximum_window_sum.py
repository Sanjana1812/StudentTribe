# Task B: Maximum Sum of a Contiguous Window
# Find the largest sum of k consecutive numbers.

def max_window_sum(numbers, k):
    # Check whether the list is empty or k is invalid.
    if not numbers:
        print("Invalid input: the list is empty.")
        return

    if k <= 0 or k > len(numbers):
        print("Invalid input: k must be between 1 and the list length.")
        return

    max_sum = None

    # Choose where each window starts.
    for i in range(len(numbers) - k + 1):
        total = 0

        # Add the numbers inside this window.
        for j in range(i, i + k):
            total = total + numbers[j]

        # Keep the biggest sum found so far.
        if max_sum is None or total > max_sum:
            max_sum = total

    print("Maximum window sum:", max_sum)


# Test case 1
numbers = [2, 1, 5, 1, 3, 2]
k = 3
max_window_sum(numbers, k)  # Expected: 9

# Test case 2
numbers = [4, 2, 7, 1, 5]
k = 3
max_window_sum(numbers, k)  # Expected: 13

# Test case 3: k = 1
numbers = [4, 2, 7]
k = 1
max_window_sum(numbers, k)  # Expected: 7

# Test case 4: k equals the list length
numbers = [3, 6, 2]
k = 3
max_window_sum(numbers, k)  # Expected: 11

# Test case 5: invalid k (zero)
numbers = [2, 4, 6]
k = 0
max_window_sum(numbers, k)  # Expected: invalid input message

# Test case 6: invalid k (larger than list length)
numbers = [2, 4, 6]
k = 5
max_window_sum(numbers, k)  # Expected: invalid input message

# Test case 7: empty list
numbers = []
k = 2
max_window_sum(numbers, k)  # Expected: invalid input message


# Complexity:
# Time: O(n * k), because each window adds k numbers.
# Extra space: O(1), because only a few variables are used.
