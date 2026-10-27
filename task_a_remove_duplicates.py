# Task A: Remove duplicates from a list
# Keep the original order.
# Beginner-friendly version using a loop and an empty list.

# Test case 1
numbers = [2, 3, 2, 4, 3]
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Test case 1:", result)  # Expected: [2, 3, 4]


# Test case 2: No duplicates
numbers = [1, 2, 3, 4]
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Test case 2:", result)  # Expected: [1, 2, 3, 4]


# Test case 3: All numbers are duplicates
numbers = [2, 2, 2]
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Test case 3:", result)  # Expected: [2]


# Test case 4: Empty list
numbers = []
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Test case 4:", result)  # Expected: []


# Test case 5: Mixed duplicates
numbers = [3, 1, 3, 2, 1]
result = []

for number in numbers:
    if number not in result:
        result.append(number)

print("Test case 5:", result)  # Expected: [3, 1, 2]
