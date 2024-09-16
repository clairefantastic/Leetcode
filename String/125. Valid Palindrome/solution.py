class Solution:
    def isPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1
        lowerString = s.lower()
        while l < r:
            while l < r and not lowerString[l].isalnum():
                l += 1
            while l < r and not lowerString[r].isalnum():
                r -= 1
            if lowerString[l] == lowerString[r]:
                l += 1
                r -= 1
            else:
                return False
        return True
