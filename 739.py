#case 1 stack ka approch
class DailyTemperatures:
    def dailyTemperatures(self, temperatures):
        helper_stack = []

        n = len(temperatures)
        result = [0] * n

        for idx in range(n - 1, -1, -1):
            # Popping all indices with a lower or equal
            # temperature than the current index
            while helper_stack and temperatures[idx] >= temperatures[helper_stack[-1]]:
                helper_stack.pop()

            # If the stack still has elements,
            # then the next warmer temperature exists!
            if helper_stack:
                result[idx] = helper_stack[-1] - idx

            # Inserting current index in the stack
            helper_stack.append(idx)

        return result

# Example usage:
# temperatures = [73, 74, 75, 71, 69, 72, 76, 73]
# solution = DailyTemperatures()
# result = solution.dailyTemperatures(temperatures)
# print(result)

#case 2 time issue
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        temp = temperatures
        result = []

        for i in range(len(temp)):
            j = i + 1
            while j < len(temp) and temp[j] <= temp[i]:
                j += 1

            if j < len(temp):
                result.append(j - i)
            else:
                result.append(0)

        return result
    
#case 3
class Solution:
    def dailyTemperatures(self, temperatures):
        n = len(temperatures)
        hottest = float('-inf')
        ans = [0] * n

        for i in range(n - 1, -1, -1):
            if temperatures[i] >= hottest:
                hottest = temperatures[i]
            else:
                it = i + 1
                while it < n and temperatures[it] <= temperatures[i]:
                    it += ans[it]
                ans[i] = it - i if it < n else 0

        return ans
    