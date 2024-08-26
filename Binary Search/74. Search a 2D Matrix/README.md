74. Search a 2D Matrix

- Link: https://leetcode.com/problems/search-a-2d-matrix/description/
- Difficulty: Medium 
- Topics: Array, Binary Search, Matrix

You are given an m x n integer matrix matrix with the following two properties:

- Each row is sorted in non-decreasing order.
- The first integer of each row is greater than the last integer of the previous row.
Given an integer target, return true if target is in matrix or false otherwise.

You must write a solution in O(log(m * n)) time complexity.

Example 1:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
Output: true

Example 2:
Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
Output: false

Constraints:

- m == matrix.length
- n == matrix[i].length
- 1 <= m, n <= 100
- -10^4 <= matrix[i][j], target <= 10^4

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input matrix be empty? (We don't need to consider empty inputs)
2. Any requirement on time/space complexity? (O(log(m*n)) in time and O(1) in space)
3. Can the row size be different from the column size? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search
    - Binary search is a method for locating an element in a sorted list efficiently. Searching for an element can be done naively in O(N) time, but binary search speeds it up to O(logN) time.

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General idea: Consider 2D as 1D and we can simply apply binary search to search for the target
    - Determine the number of rows and columns by obtaining lengths, allowing us the calculate the total number of elements using rows multiplied by columns
    - Define the mid_value as matrix[mid//columns][mid%columns]
    - If mid_value is greater than the target, adjust the right pointer
    - If mid_value is less than the target, adjust the left pointer
    - If a mid_value equal to the target is successfully found, return True; otherwise, return False
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume given a m * n integer matrix
- Time Complexity: O(log(m*n))
- Space Complexity: O(1)
