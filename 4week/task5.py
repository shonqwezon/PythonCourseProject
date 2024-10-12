"""
leetcode.com/problem-list/prefix-sum/
url: https://leetcode.com/problems/continuous-subarray-sum/
"""


class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        dp = [0]
        for i in range(len(nums)):
            dp.append((dp[-1] + (nums[i] % k)) % k)
        hash = {}
        for i in range(len(dp)):
            if dp[i] in hash:
                if i - hash[dp[i]] > 1:
                    return True
            else:
                hash[dp[i]] = i

        return False


if __name__ == "__main__":
    s = Solution()
    print(s.checkSubarraySum([1, 0, 1, 0, 1], 4))
