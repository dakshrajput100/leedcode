""" for loop me nahi hoga q ki index error aagyega
mtlb traget value ko nums se delete krna hai 
or fir len of list return krna hai """
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return i
        #return len(nums)
    


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        j = 0 
        for i in range(len(nums)):
            if num[i] != val:
                nums[k] = nums[i]
                k+=1
        return k
        #return len(nums)    