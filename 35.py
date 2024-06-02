class Solution:
    def searchInsert(self, nums, target):
        start = 0
        end = len(nums) - 1

        while start <= end:
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                end = mid - 1
            else:
                start = mid + 1

        return end+1

"""
condition false hoga tb hoga jb start pointer bara hoga end pointer se 
mtlb wo ek dusre ko cross kia tha 
so hmlog ko to chahiye tha start +1 return krna tha jb koi element nahi mil rha tha 
but ab jb yhe cross kr gya hai starting pointer equal hogya hai start+1 ke sb hmlog 
return kr denge start pointer
"""