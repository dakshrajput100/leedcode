class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        for i in range(len(a)):
             
            if a[i] != b[i]:
                return(c)
            else:    
                c = c + a[i]
               
        return(c)       
    
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        for i in range(len(a)):
             
            if a[i] != b[i]:
                return c
                
            c = c + a[i]
               
        return c

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
       

        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        i = 0

        while i < len(a) and i < len(b):
            if a[i] == b[i]:
                c += a[i]
                i += 1
            else:
                break

        return c



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        s = sorted(strs)
        j = s[0]
        k = s[-1]
        z = ""
        i = 0
        while i < len(j) and i < len(k):
            if j[i] != k[i]:
                return z
            z += j[i]
            i +=1
        return z             

#code issue

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        while(True):
            i = 0
            if a[i] == b[i]:
                c = c + a[i]
                i = i+1
            return c
        
        return c

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        strr = sorted(strs)
        a = strr[0]
        b = strr[-1]
        c = ""
        while(True):
            i = 0
            if a[i] == b[i]:
                c = c + a[i]
                i = i+1
            return c
        return c