class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        curmax = 0
        gmax = nums[0]
        curmin = 0
        total = 0
        gmin = nums[0]
        for i in nums:
            curmax = max(curmax+i,i)
            gmax = max(curmax,gmax)
            total += i
            curmin = min(curmin +i,i)
            gmin = min(gmin,curmin)
        return max(gmax,total-gmin) if gmax >0 else gmax
            