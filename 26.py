"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        
        j = 1
        for i in range(len(nums) - 1):
            if nums[i] != nums[i+1]:
                nums[j] = nums[i+1]
                j = j+1
        return j    
   """           
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 0
        j = 0
        while(j<len(nums)):
            if nums[i] != nums[j]:
                nums[i+1],nums[j] = nums[j], nums[i+1]
                i = i+1
                j = j+1
            else:
                j = j+1    
        return i+1
   