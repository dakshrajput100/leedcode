import math
class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        d = abs(dividend)
        dd = abs(divisor)
        s = d/dd

        if dividend <0 or divisor < 0:
            s = s * (-1)
        if dividend <0 and divisor < 0:
            s = abs(s)    
        if (s>= -2 **31 and s<= 2 **31-1 ):
            return (math.trunc(s))
        return 2147483647      