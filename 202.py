class Solution:
    def isHappy(self, n: int) -> bool:
        mp = {}
        while True:
            g = str(n)
            if g in mp:
                return False
            else:
                mp[g] = g
                n = sum(int(i) ** 2 for i in g)
                if n == 1:
                    return True
                
class Solution:
    def isHappy(self, n: int) -> bool:
        mp = {}
       
        while True:
            g = str(n)
            if g in mp:
                return False
            else:
                mp[g] = g
                
                n = 0
                for i in g:
                    n += int(i)**2
                if n == 1:
                    return True    

        