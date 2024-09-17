class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashtable_s = {}
        hashtable_t = {}
        for c in s:
            if c in hashtable_s:
                hashtable_s[c] += 1
            else:
                hashtable_s[c] = 1
        for c in t:
            if c in hashtable_t:
                hashtable_t[c] += 1
            else:
                hashtable_t[c] = 1
        return hashtable_s == hashtable_t
