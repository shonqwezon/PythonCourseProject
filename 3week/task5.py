"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/maximum-subarray
"""


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        for i in range(1, len(nums)):
            nums[i] = max(nums[i], nums[i] + nums[i - 1])
        return max(nums)


if __name__ == "__main__":
    s = Solution()
    print(s.maxSubArray([1, 2, -1, -2, 2, 1, -2, 1, 4, -5, 4]))
