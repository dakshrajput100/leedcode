#case1
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False  
        if x >= 0:
            h = str(x)
            l = len(h)
            
            for i in range(l // 2):  
                if h[i] != h[l - i - 1]:  
                    return False 
            return True  
#case2

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False
            
        i = 0
        l = str(x)
        j = len(l) - 1 
        while i <= j: # Corrected the condition
            if l[i] != l[j]:
                return False
            i += 1
            j -= 1    
        return True
