class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        l,total = 0,0
        res = float("inf")
        
        for r in range(len(nums)):
            total += nums[r]
            while total >= target:
                res = min(r - l + 1, res)  # Change 'r - 1 + 1' to 'r - l + 1'
                total -= nums[l]  # Change 'nums[1]' to 'nums[l]'
                l += 1  # Increment the left pointer
                
        return 0 if res == float("inf") else res
