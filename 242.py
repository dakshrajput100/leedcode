#case1
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        arr = [0]*26
        for i in s:
            arr[ord(i) - ord("a")] += 1
        for j in t:
            arr[ord(j) - ord("a")] -= 1
        for z in arr:
            if z != 0:
                return False    
        return True    

#case2
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        mp = {}
        for i in s:
            mp[i] = mp.get(i,0) + 1
        for i in t:
            if i not in mp or mp[i] == 0:
                return False
            mp[i] -=1
        return True                         

#casen3

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        mp = defaultdict(int)
        
        for char in s:
            mp[char] += 1
        
        for char in t:
            mp[char] -= 1
        
        return all(count == 0 for count in mp.values())
    