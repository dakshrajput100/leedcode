class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = self.findLeftBound(nums, target)
        right = self.findRightBound(nums, target)
        return [left, right]

    def findLeftBound(self, nums: List[int], target: int) -> int:
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2 # mid = high - low  // 2

            if nums[mid] == target:
                index = mid
                high = mid - 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index

    def findRightBound(self, nums: List[int], target: int) -> int:
        index = -1
        low, high = 0, len(nums) - 1

        while low <= high:
            mid = low + (high - low) // 2

            if nums[mid] == target:
                index = mid
                low = mid + 1
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1

        return index
