#case 1
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j, count = 0, 0, 0  # Corrected variable name from 'c' to 'count'
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
                j += 1
                count += 1
            else:
                j += 1
        if count == len(s):  # Corrected variable name from 'count' to 'count'
            return True
        else:
            return False

#case2
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i, j = 0, 0
        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1
        return i == len(s)
        