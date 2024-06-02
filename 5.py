#case 1 time issue
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s, start, end):
            if start >= end:
                return True
            return s[start] == s[end] and is_palindrome(s, start + 1, end - 1)

        def countt(s):
            palindromes = []

            for i in range(len(s)):
                for j in range(i, len(s)):
                    if is_palindrome(s, i, j):
                        palindromes.append(s[i:j+1])

            palindromes.sort(key=len)  # Sort the palindromes by length
              # Check if there are any palindromes found
            return palindromes[-1]  # Return the longest palindrome
        return countt(s)
    
#case2 time limit
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def is_palindrome(s, start, end):
            if start >= end:
                return True
            return s[start] == s[end] and is_palindrome(s, start + 1, end - 1)
        z = " "
        i = 0
        j = len(s)-1
        while i <=j:
            if s[i] != s[j]:
                j -=1
            elif s[i] == s[j]:
                if is_palindrome(s,i,j):
                    z = s[i:j]
        return z

#case3 final
class Solution:
    def longestPalindrome(self, s: str) -> str:
        s = s
        if len(s) <= 1:
            return s

        longest_palindrome = ""

        for i in range(1, len(s)):
            # Consider odd length
            low = i
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1

            palindrome = s[low + 1:high]
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

            # Consider even length
            low = i - 1
            high = i
            while low >= 0 and high < len(s) and s[low] == s[high]:
                low -= 1
                high += 1

            palindrome = s[low + 1:high]
            if len(palindrome) > len(longest_palindrome):
                longest_palindrome = palindrome

        return longest_palindrome
                