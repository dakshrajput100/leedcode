#case 1 time limit
"""
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxx = 0
        curr = 0
        for i in range(len(height)-1):
            for j in range(1, len(height)):
                a = min(height[i], height[j])
                k = j - i
                curr = k*a
                maxx = max(maxx,curr)
               # if maxx < curr:
                #    maxx = curr
        return maxx    """  

#case 2       
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        
        while left < right:
            h = min(height[left], height[right])
            width = right - left
            max_area = max(max_area, h * width)
            
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        
        return max_area
