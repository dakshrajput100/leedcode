class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'IV': 4,'V': 5, 'IX':9, 'X': 10, 'XL':40,'L': 50,'XC':90, 'C': 100, 'CX':400, 'D': 500, 'CM': 900,'M': 1000}
        r = 0
        for i in range(len(s)):
            if i + 1 < len(s) and map[s[i]] < map[s[i+1]]:
                b = map.get(s[i])
                r = r - b
            else:
                b = map.get(s[i])
                r = r + b    
        return r
    


class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'IV': 4,'V': 5, 'IX':9, 'X': 10, 'XL':40,'L': 50,'XC':90, 'C': 100, 'CX':400, 'D': 500, 'CM': 900,'M': 1000}
        r = 0
        for i in range(len(s)):
            if i + 1 < len(s) and map[s[i]] < map[s[i+1]]:

                r = r - map.get(s[i])
            else:
                
                r = r + map.get(s[i])    
        return r
    
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'IV': 4,'V': 5, 'IX':9, 'X': 10, 'XL':40,'L': 50,'XC':90, 'C': 100, 'CX':400, 'D': 500, 'CM': 900,'M': 1000}
        r = 0
        i = 0
        while i < (len(s)):
            if i + 1 < len(s) and map[s[i]] < map[s[i+1]]:

                r = r - map[s[i]]
            else:
                
                r = r + map[s[i]] 
            i = i+1       
        return r     
 issue
class Solution:
    def romanToInt(self, s: str) -> int:
        map = {'I': 1, 'IV': 4,'V': 5, 'IX':9, 'X': 10, 'XL':40,'L': 50,'XC':90, 'C': 100, 'CX':400, 'D': 500, 'CM': 900,'M': 1000}
        r = 0
        for i in range(len(s)):
            if i + 1 < len(s) and map[s[i]] < map[s[i+1]]:

                r = r - map[s[i]]
            else:
                
                r = r + map[s[i]]    
        return r        