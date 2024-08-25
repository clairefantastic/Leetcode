23. Merge k Sorted Lists

- Link: https://leetcode.com/problems/merge-k-sorted-lists/description/
- Difficulty: Hard
- Topics: Linked List, Merge Sort

You are given an array of k linked-lists lists, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.

Example 1:
Input: lists = [[1,4,5],[1,3,4],[2,6]]
Output: [1,1,2,3,4,4,5,6]
Explanation: The linked-lists are:
[
  1->4->5,
  1->3->4,
  2->6
]
merging them into one sorted list:
1->1->2->3->4->4->5->6

Example 2:
Input: lists = []
Output: []

Example 3:
Input: lists = [[]]
Output: []
 
Constraints:

- k == lists.length
- 0 <= k <= 10^4
- 0 <= lists[i].length <= 500
- -10^4 <= lists[i][j] <= 10^4
- lists[i] is sorted in ascending order
- The sum of lists[i].length will not exceed 10^4

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Can the input be empty? (Yes)
2. Any requirement on time/space complexity? (O(nlogk) in time and O(n) in space)
3. Does the linked list have a cycle? (No)
4. Can the input lists have differing lengths? (Yes. Do not assume they will have the same length)
5. Is it acceptable to modify the input lists during the merge process, or should they remain unchanged? (Yes. It's generally acceptable to modify the input lists during the merge process)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

General Idea: This problem can be broken down into smaller, more manageable parts: 1. Merging two sorted link lists and 2. Applying this merge operation to a collection of lists. Start by solving the simpler problem of merging two sorted linked lists. This is a common problem and can be approached by comparing the head nodes of both lists and repeatedly choosing the smaller value to add to the merged list. For multiple lists, use a divide-and-conquer approach. Divide the list of linked lists into halves, merge each half, and then merge the results of these halves. This approach reduces the complexity by handling smaller portions of the problem at a time.

1. Define a class ListNode to represent a node in a linked list (Simple linked list)
2. Define a class Solution with the following methods:
3. Method mergeKLists(lists)
    - Input: an array of ListNode objects (each representing a sorted linked list)
    - Output: a single ListNode object representing the merged sorted linked list
    - If the input 'lists' is empty, return None
    - Call mergeLists with parameters 'lists', 0, and len(lists) - 1
    - Return the result of mergeLists
4. Method mergeLists(lists, start, end)
    - Input: an array of ListNode objects, start index, and end index
    - Output: a ListNode object representing a portion of the merged list
    - If start index equals end index, return lists[start]
    - Calculate mid as the midpoint between start and end
    - Recursively call merge_lists for the left half (start to mid)
    - Recursively call merge_lists for the right half (mid + 1 to end)
    - Merge the two halves using mergeTwoLists and return the result
5. Method mergeTwoLists(l1, l2)
    - Input: two ListNode objects l1 and l2
    - Output: a ListNode object representing the merged list of l1 and l2
    - Create a dummy ListNode to start the merged list
    - Set a current pointer to the dummy node
    - While both l1 and l2 have nodes:
        - Compare the values of l1 and l2
        - Attach the smaller node to 'current.next'
        - Move the 'current' pointer and the pointer of the list whose node was added
    - If either l1 or l2 still have nodes, attach the remainder to 'current.next'
    - Return 'dummy.next' (the head of the merged list)
6. In the main function or usage:
    - Create instances of ListNode representing each linked list
    - Create an instance of Solution
    - Call mergeKLists with the array of ListNode instances
    - The returned ListNode instance represents the head of the merged sorted linked list

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
- Time Complexity: O(NlogK)
- Space Complexity: O(N)
