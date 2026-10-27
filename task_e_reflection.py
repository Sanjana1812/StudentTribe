# Task E: Reflection

# Name: Sanjana
# Date: 27 October 2026
# Day: 2


# 1. My approach:
# For Task A, I used a loop to check each number and add it to the
# result list only if it was not already present.
# For Task B, I used nested loops to calculate the sum of each window.
# For Task C, I used a found variable and break to print only one result.
# For Task D, I practised using lists, sets, and dictionaries.


# 2. Test cases:

# Task A:
# [2, 3, 2, 4, 3] -> [2, 3, 4]
# [1, 2, 3, 4] -> [1, 2, 3, 4]
# [2, 2, 2] -> [2]
# [] -> []
# [3, 1, 3, 2, 1] -> [3, 1, 2]

# Task B:
# [2, 1, 5, 1, 3, 2], k = 3 -> 9
# [4, 2, 7, 1, 5], k = 3 -> 13
# [4, 2, 7], k = 1 -> 7
# [3, 6, 2], k = 3 -> 11
# k = 0 -> Invalid input
# k greater than the list length -> Invalid input
# Empty list -> Invalid input


# 3. Time and space complexity:

# Task A:
# Time: O(n^2) in the worst case because membership is checked
# in the result list.
# Extra space: O(n) for the result list.

# Task B:
# Time: O(n * k), because each window recalculates the sum of k elements.
# Extra space: O(1), because only a few variables are used.

# Task C:
# Time: O(n) in the worst case because the list may need to be
# searched completely.
# Extra space: O(1), because only a few variables are used.


# 4. What I found difficult:
# I found it difficult to understand how to calculate the maximum
# sum of consecutive numbers and how to handle invalid values of k.
# I also needed to understand how to print "Not found" only once.


# 5. What I would improve after feedback:
# I will practise more Python problems and test edge cases.
# I will trace my code with small examples before submitting it.
# I will also learn the sliding-window method to improve Task B
# from O(n * k) time to O(n) time.
