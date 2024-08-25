class ListNode:
    def __init__(self, val, prev=None, next=None):
        self.val = val
        self.prev = prev
        self.next = next

class BrowserHistory(object):

    def __init__(self, homepage):
        self.cur = ListNode(homepage)

    def visit(self, url):
        self.cur.next = ListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps):
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.val

    def forward(self, steps):
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.val
