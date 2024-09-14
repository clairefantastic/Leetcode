701. Insert into a Binary Search Tree

- Link: https://leetcode.com/problems/insert-into-a-binary-search-tree/
- Difficulty: Medium
- Topics: Binary Search Tree

You are given the root node of a binary search tree (BST) and a value to insert into the tree. Return the root node of the BST after the insertion. It is guaranteed that the new value does not exist in the original BST.

Notice that there may exist multiple valid ways for the insertion, as long as the tree remains a BST after insertion. You can return any of them.

Example 1:

Input: root = [4,2,7,1,3], val = 5
Output: [4,2,7,1,3,5]

Example 2:

Input: root = [40,20,60,10,30,50,70], val = 25
Output: [40,20,60,10,30,50,70,null,null,25]

Example 3:

Input: root = [4,2,7,1,3,null,null,null,null,null,null], val = 5
Output: [4,2,7,1,3,5]

Constraints:

- The number of nodes in the tree will be in the range [0, 10^4]
- -10^8 <= Node.val <= 10^8
- All the values Node.val are unique
- -10^8 <= val <= 10^8
- It's guaranteed that val does not exist in the original BST


UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any requirement on time/space complexity? (O(h) in time)
2. Can the tree be empty? (Yes)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Binary Search Tree Insertion

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Iteratively: Insert the node, we need to track the parent node, so we stop at the node where we insert the new node (Space complexity: O(1))
2. Recursively: Imagine the edge case that the original tree is empty, insert the node and return the root (Space complexity: O(h))

(Use recursively solution)
General Idea:
- If not root, return the new node
- If val > root.val, assign the return value of insert function applying on root.right to root.right
- Else(Since the val would not have duplicates), assign the return value of insert function applying on root.left to root.left
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
