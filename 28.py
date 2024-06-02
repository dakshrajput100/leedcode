#case 1                  
#SLIDING WINDOW #case1
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(haystack)
        n2 = len(needle)
        if n2 > n1:             #if needle == "":
            return -1                       #return 0
                       

        for i in range(n1 - n2 + 1):
        
            if haystack[i:i + n2] == needle:
                return i

        return -1

#case2

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n1 = len(haystack)
        n2 = len(needle)
        if n2 > n1:
            return -1
        
        j = 0
        i = 0
        start = 0
        while i < n1 and j < n2:
            if haystack[i] == needle[j]:
                # if i - start+1 == n2
                if j + 1 == n2:
                    return start
                j += 1
                i += 1
            else:
                j = 0
                start += 1
                i = start
        
        return -1
    
#case 3
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if needle == "":
            return 0

        for i in range(len(haystack) + 1 - len(needle)):
            for j in range(len(needle)):
                if haystack[i+j] != needle[j]:
                    break
                if j == len(needle)-1:
                    return i
        return -1              

#wrong

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        i = 0
        j = 0
        while j < len(needle):
            if haystack[i] == needle[j]:
                i +=1
                j +=1
                z = 0
                if len(needle)-1 == j:
                    
                    if needle[1] == haystack[z]:
                        return z
                    else:
                        z +=1   
            else:
                i +=1 
        return -1                      
    

