class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx =nums[0]
        sum = 0
        for i in range(len(nums)):
            sum += nums[i]
            if maxx<sum:
                maxx = max(sum,maxx)
            if sum < 0:
                sum = 0 
        return maxx        


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxx = nums[0]
        sum = 0
        for i in nums:
            sum = max(sum+i,i)
            maxx = max(sum,maxx)
            
        return maxx             