class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        n = len(nums)
        for i in range(1, n):
            if nums[i] == nums[i - 1]:
                return True
        return False
#time issue so isske niache wala
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = []
        nums.sort()
        for num in nums:
            if num in seen:
                return True
            seen.append(num)
        return False

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        #nums.sort()
        s = set()
        for i in nums:

            if i  in s:
                return True
            s.add(i)
        return False    



class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen and seen[num] >= 1:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = {}
        for num in nums:
            if num in seen:
                return True
            seen[num] = seen.get(num, 0) + 1
        return False    