class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
       
        nums.sort()  # Sort the array
        
        sum = 0
        for i in range(0, len(nums), 2):
            sum += nums[i]  # Add every even-indexed element to the sum
        
        return sum