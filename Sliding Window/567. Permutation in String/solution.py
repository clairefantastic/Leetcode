class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2) < len(s1):
            return False

        s1_count = {}
        s2_count = {}

        for c in s1:
            s1_count[c] = 1 + s1_count.get(c, 0)

        n = len(s1)
        l, r = 0, n - 1

        for c in s2[l:r]:
            s2_count[c] = 1 + s2_count.get(c, 0)

        while r < len(s2):
            s2_count[s2[r]] = 1 + s2_count.get(s2[r], 0)

            if s2_count == s1_count:
                return True

            s2_count[s2[l]] -= 1

            if s2_count[s2[l]] == 0:
                del s2_count[s2[l]]

            l += 1
            r += 1
        return False
