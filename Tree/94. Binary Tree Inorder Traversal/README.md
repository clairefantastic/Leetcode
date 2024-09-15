94. Binary Tree Inorder Traversal

- Link: https://leetcode.com/problems/binary-tree-inorder-traversal/description/
- Difficulty: Easy
- Topics: DFS

Given the root of a binary tree, return the inorder traversal of its nodes' values.

Example 1:

Input: root = [1,null,2,3]
Output: [1,3,2]

Example 2:

Input: root = [1,2,3,4,5,null,8,null,null,6,7,9]
Output: [4,2,6,5,7,1,3,9,8]

Example 3:

Input: root = []
Output: []

Example 4:

Input: root = [1]
Output: [1]

Constraints:

- The number of nodes in the tree is in the range [0, 100]
- -100 <= Node.val <= 100

Follow up: Recursive solution is trivial, could you do it iteratively?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? 
2. Can the tree be empty? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

DFS
1. Iteratively
2. Recursively

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Iteratively: Use a stack
    - Initialize a current pointer (First set to root)
    - Keep go left(cur = cur.left), add to the stack when current pointer is not None
    - If current pointer is None, pop from the stack and assign to current pointer
    - Append current pointer to the result array
    - Go right (cur = cur.right), add to the stack when current pointer is not None
    - If current pointer is None, pop from the stack
    - When the stack is empty, return the result
2. Recursively: 
    - Initialize the empty result array
    - Define the inOrder function
        - If root is None, return
        - call inOrder(root.left)
        - append the value of the root to the result array
        - call inOrder(root.right)
    - call inOrder(root)
    - return the result array
    
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
