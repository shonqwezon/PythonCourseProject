"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/arithmetic-slices/
"""


class Solution:
    def numberOfArithmeticSlices(self, nums: list[int]) -> int:
        dp = [0] * len(nums)
        res = 0

        for i in range(2, len(nums)):
            if nums[i] - nums[i - 1] == nums[i - 1] - nums[i - 2]:
                dp[i] = dp[i - 1] + 1
                res += dp[i]
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfArithmeticSlices([1, 2, 3, 4]))
