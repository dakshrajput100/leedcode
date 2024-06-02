class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        n = len(nums)
        num_set = set(nums)
        disappeared = []
        for i in range(n+1):
            if i not in num_set:
                disappeared.append(i)
        return disappeared