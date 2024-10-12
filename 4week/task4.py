"""
leetcode.com/problem-list/prefix-sum/
url: https://leetcode.com/problems/subarray-sum-equals-k/
"""

import bisect


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        hashes = {0: [0]}
        dp = [0]
        for i in range(len(nums)):
            dp.append(dp[-1] + nums[i])
            if dp[-1] not in hashes:
                hashes[dp[-1]] = []
            hashes[dp[-1]].append(i + 1)

        c = 0
        for i in range(len(dp) - 1, -1, -1):
            target = dp[i] - k
            if target in hashes:
                c += bisect.bisect_right(hashes[target], i - 1)
        return c


if __name__ == "__main__":
    s = Solution()
    print(s.subarraySum([-1, -1, 1], 0))
