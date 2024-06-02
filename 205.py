class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for i in range(len(s)):
            if s[i] not in mp:
                if t[i] not  in mp.values():
                    mp[s[i]] = t[i]
                else:
                    return False
            elif mp[s[i]] != t[i]:
                return False
        return True                        