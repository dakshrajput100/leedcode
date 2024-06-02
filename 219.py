class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        mp = {}
        for i in range(len(nums)):
            if nums[i] in mp and i - mp.get(nums[i]) <= k:
                return True
            else:
                mp[nums[i]] = i
        return False