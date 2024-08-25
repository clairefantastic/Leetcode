# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeKLists(self, lists):
        if not lists:
            return None
        return self.mergeLists(lists, 0, len(lists) - 1)

    def mergeLists(self, lists, start, end):
        # Base case of the recursion: When there is only one list
        if start == end:
            return lists[start]
        
        # Divide the lists into two parts and merge them recursively
        mid = (start + end) // 2
        left = self.mergeLists(lists, start, mid)
        right = self.mergeLists(lists, mid + 1, end)

        # Conquer the subproblems
        return self.mergeTwoLists(left, right)

    def mergeTwoLists(self, l1, l2):
        dummy = ListNode(0)
        cur = dummy

        while l1 and l2:
            if l1.val <= l2.val:
                cur.next = l1
                l1 = l1.next
            else:
                cur.next = l2
                l2 = l2.next
            cur = cur.next

        if l1:
            cur.next = l1
        if l2:
            cur.next = l2

        return dummy.next
