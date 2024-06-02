#case1
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            for j in range(len(nums)):
                for z in range(len(nums)):
                    if i !=j and i !=z and j!= z and nums[i] + nums[j] + nums[z] == 0:
                        list = [nums[i],nums[j],nums[z]]
                        a = sorted(list)
                        if a not in arr:
                            arr.append(a)
        return arr


#case 2
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        i =0
        j = 0
        while(i<len(nums)):
            for j in range(len(nums)):
            
                for z in range(len(nums)):
                    if i !=j and i !=z and j!= z and nums[i] + nums[j] + nums[z] == 0:
                        list = [nums[i],nums[j],nums[z]]
                        a = sorted(list)
                        if a not in arr:
                            arr.append(a)
                            
            i = i+1                
        return arr
#case3
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        arr = []
        for i in range(len(nums)):
            for j in range(i,len(nums)):
                for z in range(j,len(nums)):
                    if i !=j and i !=z and j!= z and nums[i] + nums[j] + nums[z] == 0:
                        list = [nums[i],nums[j],nums[z]]
                        a = sorted(list)
                        if a not in arr:
                            arr.append(a)
        return arr
    
#final
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
      
        
        A = sorted(nums)
        arr_size = len(A)
        result_set = set()

        for i in range(0, arr_size - 2):
            l = i + 1
            r = arr_size - 1

            while l < r:
                current_sum = A[i] + A[l] + A[r]

                if current_sum == 0:
                    result_set.add((A[i], A[l], A[r]))
                    l += 1
                    r -= 1
                elif current_sum < 0:
                    l += 1
                else:
                    r -= 1
                    
        result_set = [list(result_set) for result_set in result_set]
        return list(result_set)


# Example usage:


class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        s = set()
        nums.sort()

        for i in range(len(nums)-2):
            
            j = i+1
            z = len(nums) -1
            while j<z:
                current_sum = nums[i] + nums[j] +nums[z]
                if current_sum == 0:
                    s.add((nums[i], nums[j], nums[z]))

                    j +=1
                    z -=1
                elif  current_sum < 0:
                    j +=1
                else:
                    z -=1
        return s               


    