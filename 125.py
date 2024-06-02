class Solution:
    def isPalindrome(self, s: str) -> bool:
        c = ""
        for i in s:
            if i.isalnum():
                c += c.lower()
        return s == s[: :-1]

#case2
""""
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l = 0
        h = len(s)-1
        while l <= h:
            if s[l] == s[h]:
                l 
""" 
#case2
class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,h = 0 , len(s)-1
        while l < h:
            while l < h and not self.check(s[l]):
                l +=1
            while l < h and not self.check(s[h]):
                h -=1   
            if s[l].lower() != s[h].lower():
                return False
            l +=1
            h -=1        
        return True            

    def check(self,g):
        return (ord("A") <= ord(g) <= ord('Z')or ord("a") <= ord(g) <= ord('z') or ord("0") <= ord(g) <= ord('9')  )  

#case3


class Solution:
    def isPalindrome(self, s: str) -> bool:
        l,h = 0 , len(s)-1
        while l < h:
            if not self.check(s[l]):
                l +=1
                continue
            if not self.check(s[h]):
                h -=1
                continue   
            if s[l].lower() != s[h].lower():
                return False
            l +=1
            h -=1        
        return True            

    def check(self,g):
        return (ord("A") <= ord(g) <= ord('Z')or ord("a") <= ord(g) <= ord('z') or ord("0") <= ord(g) <= ord('9')  )   
         
            