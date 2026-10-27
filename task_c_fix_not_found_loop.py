# Task C: Fix the loop so "Not found" prints only once.
# Goal: Search for a number in a list.
# If the number is found, print "Found".
# If it is not found, print "Not found" only once.

numbers = [10, 20, 30, 40, 50]
target = 25

found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")


# Test case 1: Number is in the list
numbers = [10, 20, 30]
target = 20
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
# Expected: Found


# Test case 2: Number is not in the list
numbers = [10, 20, 30]
target = 25
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
# Expected: Not found


# Test case 3: Empty list
numbers = []
target = 10
found = False

for number in numbers:
    if number == target:
        found = True
        break

if found:
    print("Found")
else:
    print("Not found")
# Expected: Not found
