235. Lowest Common Ancestor of a Binary Search Tree

- Link: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree/description/
- Difficulty: Medium
- Topics: Tree, DFS, BST

Given a binary search tree (BST), find the lowest common ancestor (LCA) node of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined between two nodes p and q as the lowest node in T that has both p and q as descendants (where we allow a node to be a descendant of itself).”

Example 1:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 8
Output: 6
Explanation: The LCA of nodes 2 and 8 is 6.

Example 2:

Input: root = [6,2,8,0,4,7,9,null,null,3,5], p = 2, q = 4
Output: 2
Explanation: The LCA of nodes 2 and 4 is 2, since a node can be a descendant of itself according to the LCA definition.

Example 3:

Input: root = [2,1], p = 2, q = 1
Output: 2
 
Constraints:

- The number of nodes in the tree is in the range [2, 105].
- -10^9 <= Node.val <= 10^9
- All Node.val are unique.
- p != q
- p and q will exist in the BST.

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? (O(n) in time)
2. Can the tree be empty? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. DFS

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Start from the root node (Set a current pointer), since it is a BST, while current pointer is not None, if p and q are both larger than the current pointer, go to the right subtree (cur = cur.right), if p and q are both less than the current pointer, go the left subtree (cur = cur.left), for the other cases, return the current pointer (whether the p and q are one at the left and one at the right, or one of p and q is the root)
    
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
- Time Complexity: O(logN)
- Space Complexity: O(1)

