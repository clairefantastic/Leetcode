class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        l = 0
        maxLength = 0
        charSet = set()
        for r in range(len(s)):
            while s[r] in charSet:
                charSet.remove(s[l])
                l += 1
            charSet.add(s[r])
            maxLength = max(maxLength, r - l + 1)
        return maxLength
