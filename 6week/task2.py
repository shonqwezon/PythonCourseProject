"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-nice-subarray/
"""


class Solution:
    def longestNiceSubarray(self, nums: list[int]) -> int:
        subseq = 0
        left = 0
        mx = 0
        for i in range(len(nums)):
            if subseq & nums[i] == 0:
                subseq |= nums[i]
            else:
                while subseq & nums[i] != 0:
                    subseq ^= nums[left]
                    left += 1
                subseq |= nums[i]
            mx = max(i - left + 1, mx)
        return mx


if __name__ == "__main__":
    s = Solution()
    print(s.longestNiceSubarray([1, 3, 8, 48, 10]))
