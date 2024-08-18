707. Design Linked List

- Link: https://leetcode.com/problems/design-linked-list/description/
- Difficulty: Medium
- Topics: Linked List

Design your implementation of the linked list. You can choose to use a singly or doubly linked list. 
A node in a singly linked list should have two attributes: val and next. val is the value of the current node, and next is a pointer/reference to the next node.
If you want to use the doubly linked list, you will need one more attribute prev to indicate the previous node in the linked list. Assume all nodes in the linked list are 0-indexed.

Implement the MyLinkedList class:

- MyLinkedList() Initializes the MyLinkedList object.
- int get(int index) Get the value of the indexth node in the linked list. If the index is invalid, return -1.
- void addAtHead(int val) Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
- void addAtTail(int val) Append a node of value val as the last element of the linked list.
- void addAtIndex(int index, int val) Add a node of value val before the indexth node in the linked list. If index equals the length of the linked list, the node will be appended to the end of the linked list. If index is greater than the length, the node will not be inserted.
- void deleteAtIndex(int index) Delete the indexth node in the linked list, if the index is valid.

Example 1:
Input
["MyLinkedList", "addAtHead", "addAtTail", "addAtIndex", "get", "deleteAtIndex", "get"]
[[], [1], [3], [1, 2], [1], [1], [1]]
Output
[null, null, null, null, 2, null, 3]

Explanation
MyLinkedList myLinkedList = new MyLinkedList();
myLinkedList.addAtHead(1);
myLinkedList.addAtTail(3);
myLinkedList.addAtIndex(1, 2);    // linked list becomes 1->2->3
myLinkedList.get(1);              // return 2
myLinkedList.deleteAtIndex(1);    // now the linked list is 1->3
myLinkedList.get(1);              // return 3

Constraints:

- 0 <= index, val <= 1000
- Please do not use the built-in LinkedList library.
- At most 2000 calls will be made to get, addAtHead, addAtTail, addAtIndex and deleteAtIndex.

UMPIRE Method:

Understand

- Ask clarifying questions and use examples to understand what the interviewer wants out of this problem.
- Choose a “happy path” test input, different than the one provided, and a few edge case inputs.
- Verify that you and the interviewer are aligned on the expected inputs and outputs.

1. Any preference on single or double linked list? (Double linked list)

Match

- See if this problem matches a problem category (e.g. Strings/Arrays) and strategies or patterns within the category

1. Linked List: For linked list problems, we want to consider the following approaches:
    - Multiple Pass: If we were able to take multiple pass of the linked list, would that help solve the problem?
    - Dummy Head: Would using a dummy head as a starting point help simplify our code and handle edge cases? Dummy head would help. We won't have to consider whether we are dealing with the head, tail or middle nodes (all middle nodes)
    - Two pointer: If we used two pointers to iterate through the list at different speeds, would that help us solve this problem? 
 
Plan

- Sketch visualizations and write pseudocode
- Walk through a high level implementation with an existing diagram

1. Create a node class which has a value, a next pointer, and a previous pointer (next and prev initially null)
2. Start the list with two dummy nodes
3. Get: Use a current pointer
    - While cur exist and index > 0, cur = cur.next, index -= 1
    - If cur exist and cur != right dummy node and index == 0
        - Return the value 
        - Else return -1
4. Add node at head: Create a new node, the next node should be point at the next node of the left dummy node, the prev node should be point at the left dummy node
5. Add node at tail: Create a new node, the next node should be point at right dummy node, the prev node should be point at the previous node of the right dummy node
6. Add at index: Use a current pointer
    - While cur exist and index > 0, cur = cur.next, index -= 1
    - If cur exist and index == 0 (Don't have to care about dummy node)
        - Create a new node, the next node should be point at cur, the prev node should be point at cur.prev
7. Delete at index: Use a current pointer 
    - While cur exist and index > 0, cur = cur.next, index -= 1
    - If cur exist and cur != self.right and index == 0 
        - The next node should be point at cur.next, the prev node should be point at cur.prev

Implement

- Implement the solution (make sure to know what level of detail the interviewer wants)

See solution.py

Review

- Re-check that your algorithm solves the problem by running through important examples
- Go through it as if you are debugging it, assuming there is a bug

Evaluate

- Finish by giving space and run-time complexity
- Discuss any pros and cons of the solution

- Time complexity: O(1)
- Space complexity: O(1)
