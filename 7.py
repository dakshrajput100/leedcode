class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        s = 0
        while a:
            d =  a%10
            a = a//10
            s = s*10 +d
        if (x<0):
            s = s * (-1)
        if (s>= -2 **31 and s<= 2 **31-1 ):
            return s
        return 0        





class Solution:
    def reverse(self, x: int) -> int:
        a = abs(x)
        s = ''
        while a:
            d =  a % 10
            a = a // 10
            s = s + str(d)
        
        if x < 0:
            s = '-' + s
        
        # Checking if the reversed number is within the range of 32-bit signed integer
        if int(s) >= -2 ** 31 and int(s) <= 2 ** 31 - 1:
            return int(s)
        
        return 0
