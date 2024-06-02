#case 1
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        res = []
        p = path.split("/")
        
        for i in range(len(p)):
            if stack and p[i] == "..":
                stack.pop()
            elif p[i] and p[i] != "." and p[i] != "..":
                stack.append(p[i])

        if not stack:
            return "/"
        
        while stack:
            res.insert(0, stack.pop())
            res.insert(0, "/")

        return "".join(res)

#case2
class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        cur = ""

        for c in path + "/":
            if c == "/":
                if cur == "..":
                    if stack:
                        stack.pop()
                elif cur != "." and cur != "":
                    stack.append(cur)
                cur = ""
            else:
                cur += c

        return "/" + "/".join(stack)


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        p = path.split("/")
        res = []
        for i in p :
            if stack and i == '..' :
                stack.pop()
            elif i and i != '.' and i != '..' :
                stack.append(i)
        if not stack:
            return "/"
        
        return "/" + "/".join(stack)           
