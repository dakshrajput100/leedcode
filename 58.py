class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split(' ')[-1])
    

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        return len(s.strip().split( )[-1])    
    
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
       return len(s.split()[-1])    

#case3
class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        length = 0
        n = len(s) - 1
        
        for i in range(n, -1, -1):
            if s[i] != " ":
                count += 1
            elif count != 0:
                length = count
                break
                
        return count if length == 0 else length  

#case4
    class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        
        n = len(s) - 1
        
        for i in range(n, -1, -1):
            if s[i] != " ":
                count += 1
            elif count != 0:
                
                break
                
        return countS     