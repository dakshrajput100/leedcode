from typing import List

class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arr = sorted(arr)
        counts = []
        count = 1
        
        for i in range(1, len(arr)):
            if arr[i-1] == arr[i]:
                count += 1
            else:
                counts.append(count)
                count = 1 
        counts.append(count)  
        
        return len(set(counts)) == len(counts)
