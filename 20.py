class Solution:
    def isValid(self, s: str) -> bool:
        ss = {")":"(", "}":"{","]":"[" }
        stack = []
        for i in range(len(s)):
            if s[i] in "}])":
               #if stack           and stack[-1] == ss[s[i]]:
                if len(stack) != 0 and stack[-1] == ss[s[i]]:
                    stack.pop()
                else:                     #else:
                    return False               #stack.append(s[i])  
                    

            else:
                stack.append(s[i]) 

        #return True if not stack else False ( same as last 4 line)
        if len(stack) ==0:
            return True
        else:
            return False

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in ")]}":
                if stack and stack[-1] == "(" and s[i] == ")":  # Check for corresponding opening parenthesis
                    stack.pop()
                elif stack and stack[-1] == "{" and s[i] == "}":  # Check for corresponding opening curly brace
                    stack.pop()
                elif stack and stack[-1] == "[" and s[i] == "]":  # Check for corresponding opening square bracket
                    stack.pop()
                else:
                    return False
            else:
                stack.append(s[i])
        if stack:
            return False
        else:
            return True    
        
        #return not stack
