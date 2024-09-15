230. Kth Smallest Element in a BST

- Link: https://leetcode.com/problems/kth-smallest-element-in-a-bst/description/
- Difficulty: Medium
- Topics: DFS

Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.

Example 1:

Input: root = [3,1,4,null,2], k = 1
Output: 1

Example 2:

Input: root = [5,3,6,2,4,null,null,1], k = 3
Output: 3

Constraints:

- The number of nodes in the tree is n
- 1 <= k <= n <= 10^4
- 0 <= Node.val <= 10^4

Follow up: If the BST is modified often (i.e., we can do insert and delete operations) and you need to find the kth smallest frequently, how would you optimize?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? 
2. Can the tree be empty? 

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

DFS
1. Iteratively
2. Recursively

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Iteratively: Use a stack
    - Set n = 0
    - Initialize a current pointer (First set to root)
    - Keep go left(cur = cur.left), add to the stack when current pointer is not None
    - If current pointer is None, pop from the stack and assign to current pointer
    - n += 1
    - If n == k, return the current pointer
    - Else, go right (cur = cur.right), add to the stack when current pointer is not None
    - If current pointer is None, pop from the stack
2. Recursively: 
    - Initialize the empty result array
    - Define the inOrder function
        - If root is None, return
        - call inOrder(root.left)
        - append the value of the root to the result array
        - call inOrder(root.right)
    - call inOrder(root)
    - return the k - 1 th element in the result array
    
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
