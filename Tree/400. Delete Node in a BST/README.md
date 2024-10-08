450. Delete Node in a BST

- Link: https://leetcode.com/problems/delete-node-in-a-bst/description/
- Difficulty: Medium
- Topics: Binary Search Tree

Given a root node reference of a BST and a key, delete the node with the given key in the BST. Return the root node reference (possibly updated) of the BST.

Basically, the deletion can be divided into two stages:

1. Search for a node to remove.
2. If the node is found, delete the node.

Example 1:

Input: root = [5,3,6,2,4,null,7], key = 3
Output: [5,4,6,2,null,null,7]
Explanation: Given key to delete is 3. So we find the node with value 3 and delete it.
One valid answer is [5,4,6,2,null,null,7], shown in the above BST.
Please notice that another valid answer is [5,2,6,null,4,null,7] and it's also accepted.

Example 2:

Input: root = [5,3,6,2,4,null,7], key = 0
Output: [5,3,6,2,4,null,7]
Explanation: The tree does not contain a node with value = 0.

Example 3:

Input: root = [], key = 0
Output: []

Constraints:

- The number of nodes in the tree is in the range [0, 10^4]
- -10^5 <= Node.val <= 10^5
- Each node has a unique value
- root is a valid binary search tree
- -10^5 <= key <= 10^5

Follow up: Could you solve it with time complexity O(height of tree)?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? (O(h) in time)
2. Can the tree be empty?

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search Tree removal

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Define a function to find the minimum value of a BST
2. 
- If not root, return the root
- If val > root.val, assign the return value of remove function applying on root.right to root.right
- Else if val < root.val, assign the return value of insert function applying on root.left to root.left
- Else: 
    - If root.left is None, return root.right
    - Else if root.right is None, return root.left
    - Else, find the min node of the root.right (the right subtree), replace the root value with the min node value, and assign the return value of remove function applying on roof.right to root.right
- Return the root
    
    
Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume h is the height of the tree
- Time Complexity: O(h)
- Space Complexity: O(h)
