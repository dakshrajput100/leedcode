#using two pointer
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        
        for i in range(2, n + 1):
            lastString = ans
            l = len(ans)
            j = 0
            ans = ""
            
            while j < l:
                count = j
                while count < l and lastString[j] == lastString[count]:
                    count += 1
                
                ans += str(count - j) + lastString[j]
                j = count
            
        return ans
#best
#using one pinter and same l ke place pr len(arr)
class Solution:
    def countAndSay(self, n: int) -> str:
        anr = "1"
        
        for i in range(2, n + 1):
            arr = anr
            j = 0
            anr = ""
            
            while j < len(arr):
                count = 1
                while j + 1 < len(arr) and arr[j] == arr[j + 1]:
                    count += 1
                    j += 1
                
                anr += str(count) + arr[j]
                j += 1
            
        return anr

#using two pointer and count, count ke place pr c hai jo count kr rha hai
class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        
        for i in range(2, n + 1):  for i in range(n-1):
            lastString = ans
            l = len(ans)
            j = 0
            ans = ""
            
            while j < l:
                count = j
                c = 0
                while count < l and lastString[j] == lastString[count]:
                    c += 1
                    count +=1
                    
                ans += str(c) + lastString[j]
                j = count
            
        return ans


class Solution:
    def countAndSay(self, n: int) -> str:
        ans = "1"
        
        for i in range(2, n + 1):
            lastString = ans
            l = len(ans)
            j = 0
            ans = ""
            count = 0
            
            while j < l:
                
                c = 0
                while count < l and lastString[j] == lastString[count]:
                    c += 1
                    count +=1
                    
                ans += str(c) + lastString[j]
                j = count
                
            
        return ans        