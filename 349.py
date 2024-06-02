class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        s = set(nums1)
        g = set(nums2)
        d = []
        for i in s:
            if i in g:
                d.append(i)
        return d        
