"""
leetcode.com/problem-list/prefix-sum/
url: https://leetcode.com/problems/subarray-sum-equals-k/
"""

import bisect


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hashes = {}
        dp = [0]
        for i in range(len(nums)):
            dp.append(dp[-1] + nums[i])

        c = 0
        for i in range(len(dp)):
            target = dp[i] - k
            if target in hashes:
                c += hashes[target]
            hashes[dp[i]] = hashes.get(dp[i], 0) + 1
        return c


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([-1, -1, 1], 0))
