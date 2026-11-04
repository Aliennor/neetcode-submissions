class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = {}
        for i in range(len(s)):
            if s[i] not in a:
                a[s[i]] = 0
            a[s[i]] += 1
        
        for i in range(len(t)):
            if t[i] not in a:
                a[t[i]] = 0
            a[t[i]] -= 1

        for j in a:
            if a[j] != 0:
                return False

        return True