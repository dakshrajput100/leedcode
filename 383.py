#case1
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        arr = [0] * 26
        
        for ch in magazine:
            arr[ord(ch) - ord('a')] += 1
        
        for ch in ransomNote:
            if arr[ord(ch) - ord('a')] == 0:
                return False
            arr[ord(ch) - ord('a')] -= 1
            
        return True


#case2
class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        # Create a dictionary to count occurrences of characters in magazine
        magazine_counts = {}
        for ch in magazine:
            magazine_counts[ch] = magazine_counts.get(ch, 0) + 1
        
        # Check if ransomNote can be formed
        for ch in ransomNote:
            if ch not in magazine_counts or magazine_counts[ch] <= 0:
                return False
            magazine_counts[ch] -= 1
            
        return True

# Example usage:
solution = Solution()
print(solution.canConstruct("aa", "aab"))  # Output: True
    