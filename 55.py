from typing import List

class Solution:
    def jump(self, nums: List[int]) -> int:
        total_jumps = 0
        destination = len(nums) - 1
        coverage, last_jump_idx = 0, 0

        # Base case
        if len(nums) == 1:
            return 0

        # Greedy strategy: extend coverage as long as possible
        for i in range(len(nums)):
            coverage = max(coverage, i + nums[i])

            if i == last_jump_idx:
                last_jump_idx = coverage
                total_jumps += 1

                # Check if we reached destination already
                if coverage >= destination:
                    return total_jumps

        return total_jumps

# Example usage:
nums = [2, 3, 1, 1, 4]
solution = Solution()
result = solution.jump(nums)
print(result)
