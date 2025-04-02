148. Sort List

- Link: https://leetcode.com/problems/sort-list/description/
- Difficulty: Medium
- Topics: Linked List, Two Pointers, Divide and Conquer, Sorting, Merge Sort

Given the head of a linked list, return the list after sorting it in ascending order.

Example 1:
Input: head = [4,2,1,3]
Output: [1,2,3,4]

Example 2:
Input: head = [-1,5,3,4,0]
Output: [-1,0,3,4,5]

Example 3:
Input: head = []
Output: []

Constraints:

- The number of nodes in the list is in the range [0, 5 * 10^4].
- -10^5 <= Node.val <= 10^5

Follow up: Can you sort the linked list in O(n logn) time and O(1) memory (i.e. constant space)?

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (Yes)
2. Any requirement on time/space complexity? (O(NlogN) in time and O(N) in space)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Merge Sort
   - Pros: Great Time complexity (O(NLogN))
   - Cons: Takes O(N) memory
2. Quick Sort
   - Pros: Takes O(1) memory

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Merge Sort:
   Split the array into two halves until each half has only one element. Merge them back for the smaller values first following the larger values. Do it recursively.

Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

1. Merge Sort
   Assume N elements in nums array

- Time Complexity: O(NLogN)
- Space Complexity: O(N)
