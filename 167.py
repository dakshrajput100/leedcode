
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i, j = len(numbers) - 1, 0
        while i > j:
            if numbers[i] + numbers[j] == target:
                return [j+1 , i+1]
            elif numbers[i] + numbers[j] < target:
                j += 1
            else:
                i -= 1
        #return []