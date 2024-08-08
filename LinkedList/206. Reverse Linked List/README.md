206. Reverse Linked List

- Link: https://leetcode.com/problems/reverse-linked-list/description/
- Difficulty: Easy
- Topics: Linked List

Given the head of a singly linked list, reverse the list, and return the reversed list.

Follow up: A linked list can be reversed either iteratively or recursively. Could you implement both?

Example 1:
Input: head = [1,2,3,4,5]
Output: [5,4,3,2,1]

Example 2:
Input: head = [1,2]
Output: [2,1]

Example 3:
Input: head = []
Output: []

Constraints:

- The number of nodes in the list is the range [0, 5000].
- -5000 <= Node.val <= 5000

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (head is null?) (Yes)
2. Any requirement on time/space complexity (O(n) in time and O(1) in space)
3. Does the linked list have a cycle? (No)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Linked List: For linked list problems, we want to consider the following approaches:
    - Multiple Pass: If we were able to take multiple pass of the linked list, would that help solve the problem? This may help us determine the length of the list. However, we do not need the length of the list.
    - Dummy Head: Would using a dummy head as a starting point help simplify our code and handle edge cases? There are no edge cases that a dummy head would help handle.
    - Two pointer: If we used two pointers to iterate through the list at different speeds, would that help us solve this problem? Two pointers could help us in this problem. How could we use two different pointers in this problem? A previous point and a current pointer.
 
Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: Initialize a previous node, current node, and a next node. We will then point the current node .next to the previous node and move the previous node to current node and current node to next node and repeat the process.

1. Initialize a previous node (Initially null) and a current node
2. While current node is not null
    - Initialize next node to temporarily hold the next node
    - Point current node .next to previous node 
    - Set prev node to current node
    - Set current node to next node
3. Return previous node (New head)

Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the number of nodes in the linked list.

- Time complexity: O(N)
- Space complexity: O(1)
