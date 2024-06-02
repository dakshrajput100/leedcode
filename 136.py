
class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        arr = nums
        arr.sort()
        i = 0
        n = len(arr)     
        while i < n:
            if (i == 0 or arr[i] != arr[i-1]) and (i == n-1 or arr[i] != arr[i+1]):
                return arr[i]
            i += 1



class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        return 2 * sum(set(nums)) - sum(nums)