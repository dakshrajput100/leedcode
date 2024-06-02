class Solution:
    def majorityElement(self, nums: List[int]) -> int
        nums.sort()
        count = 1
        maxcount = 0
        j = nums[0]
        for i in range(len(nums) - 1):  # Iterate until the second-to-last index
            if nums[i] == nums[i+1]:  # Check if the current element is equal to the next one
                count += 1
                if maxcount < count:
                    maxcount = count
                    j = nums[i]
            else:
                count = 1
        return j
