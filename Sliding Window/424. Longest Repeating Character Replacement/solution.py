class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxLength = 0
        l = 0
        frequencyMap = {}
        for r in range(len(s)):
            frequencyMap[s[r]] = 1 + frequencyMap.get(s[r], 0)
            while (r - l + 1) - max(frequencyMap.values()) > k:
                frequencyMap[s[l]] -= 1
                l += 1
            maxLength = max(maxLength, r - l + 1)
        return maxLength
