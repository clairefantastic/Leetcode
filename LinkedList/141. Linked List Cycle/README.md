141. Linked List Cycle

- Link: https://leetcode.com/problems/linked-list-cycle/description/
- Difficulty: Easy
- Topics: Linked List

Given head, the head of a linked list, determine if the linked list has a cycle in it.

There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

Return true if there is a cycle in the linked list. Otherwise, return false.

Example 1:
Input: head = [3,2,0,-4], pos = 1
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 1st node (0-indexed).

Example 2:
Input: head = [1,2], pos = 0
Output: true
Explanation: There is a cycle in the linked list, where the tail connects to the 0th node.

Example 3:
Input: head = [1], pos = -1
Output: false
Explanation: There is no cycle in the linked list.
 
Constraints:

- The number of the nodes in the list is in the range [0, 104].
- -10^5 <= Node.val <= 10^5
- pos is -1 or a valid index in the linked-list.

Follow up: Can you solve it using O(1) (i.e. constant) memory?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? 
2. Any requirement on time/space complexity? (O(n) in time and O(n) in space)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Hashing: We can save all the nodes we passed into a hashset and if we encounter a same node again, this means there is a cycle in the linked list
2. Floyd's Tortoise & Hare: Declare two pointers, a slow pointer and a fast pointer, the two pointers will meet eventually if there is a cycle. This takes only O(1) space

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Declare two pointers, fast and slow, initialize both of them at the head
2. While fast and fast.next are not None
    - Slow increases one step one time, fast increases two steps one time,
    - If fast equals slow, return True,
3. Otherwise return False


Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

Assume N represents the number of nodes across all linked lists and K represents the number of linked lists.
- Time Complexity: O(N)
- Space Complexity: O(1)

