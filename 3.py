#case1
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        i, j = 0, 0
        char_set = []

        while j < len(s):
            if s[j] not in char_set:
                char_set.append(s[j])
                j += 1
                max_length = max(max_length, len(char_set))
            else:
                char_set.remove(s[i])
                i += 1

        return max_length
    
#case2    error in input pvpf

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        j = 0
        char_set = []

        while j < len(s):
            if s[j] not in char_set:
                char_set.append(s[j])
                j += 1
                max_length = max(max_length, len(char_set))
            else:
                char_set.clear()
                

        return max_length
#case 2 error
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max = 0
        for i in range(len(s)-1):
            count = 1
            for j in range(i+1,len(s)):
                
                if s[i] != s[j] and s[j-1] != s[j]:
                    count = count +1
                else:
                    break

            if max<count:
                max = count
        return max             