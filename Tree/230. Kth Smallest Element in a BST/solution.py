# Recursively method

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def inOrder(root):
            if not root:
                return
            inOrder(root.left)
            res.append(root.val)
            inOrder(root.right)

        inOrder(root)
        return res[k - 1]

# Iteratively method

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        n = 0
        stack = []
        cur = root

        while cur or stack:
            while cur:
                stack.append(cur)
                cur = cur.left
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            cur = cur.right