class Solution:
    def addBinary(self, a: str, b: str) -> str:
        n = int(a,2)
        m = int(b,2)
        a = m + n
        a =format(a, 'b')
        return a
        