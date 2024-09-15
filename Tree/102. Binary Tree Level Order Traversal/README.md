102. Binary Tree Level Order Traversal

- Link: https://leetcode.com/problems/binary-tree-level-order-traversal/description/
- Difficulty: Medium
- Topics: BFS

Given the root of a binary tree, return the level order traversal of its nodes' values. (i.e., from left to right, level by level).

Example 1:

Input: root = [3,9,20,null,null,15,7]
Output: [[3],[9,20],[15,7]]

Example 2:

Input: root = [1]
Output: [[1]]

Example 3:

Input: root = []
Output: []

Constraints:

- The number of nodes in the tree is in the range [0, 2000]
- -1000 <= Node.val <= 1000

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? (O(n) in time)
2. Can the tree be empty? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. BFS

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Declare a result array
2. Declare a queue and append the root
3. While the queue is not empty
    - Declare a level array for each level
    - Iterate through the queue
        - Pop the most left element as the current pointer
        - Add the current pointer value to the level array
        - Add the cur.left to the queue
        - Add the cur.right to the queue
    - If the level array is not empty, append the level array to the result array
4. Return the result array
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N is total number of nodes in the tree
- Time Complexity: O(N)
- Space Complexity: O(N)
