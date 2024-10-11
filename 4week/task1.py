"""
leetcode.com/problem-list/prefix-sum/
url: https://leetcode.com/problems/minimum-size-subarray-sum
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        dp = [0]
        for i in nums:
            dp.append(dp[-1] + i)

        left = 0
        right = 0
        min_dif = (len(dp) + 1, target)
        seg = target
        while True:
            seg = dp[right] - dp[left]
            if seg >= target:
                min_dif = min(min_dif, (right - left, seg - target))
                if seg == target and right + 1 < len(dp):
                    right += 1
                else:
                    left += 1
            elif seg < target:
                right += 1
                if right == len(dp):
                    break
        return 0 if min_dif[0] > len(dp) else min_dif[0]


if __name__ == "__main__":
    s = Solution()
    print(s.minSubArrayLen(4, [1, 1, 1, 1, 3]))
