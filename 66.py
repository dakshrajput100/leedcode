class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        
        summ = "".join(str(d) for d in digits)
        
        summ = str(int(summ) + 1)
        
        result = [int(d) for d in summ]
        
        return result
