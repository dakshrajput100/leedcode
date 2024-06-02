class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s_words = s.split()
        
        if len(pattern) != len(s_words):
            return False
        
        char_map = {}  # Maps characters in pattern to words in s
        
        for i in range(len(pattern)):
            if pattern[i] not in char_map:
                if s_words[i] not in char_map.values():
                    char_map[pattern[i]] = s_words[i]
                else:
                    return False
            elif char_map[pattern[i]] != s_words[i]:
                return False
        
        return True
