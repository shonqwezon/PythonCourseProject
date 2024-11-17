"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
"""


class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        mx = 0
        h = set()
        s = 0
        left = 0
        for i in range(len(nums)):
            if i - left == k:
                mx = max(mx, s)
                s -= nums[left]
                h.remove(nums[left])
                left += 1
            if nums[i] not in h:
                h.add(nums[i])
                s += nums[i]
            else:
                while nums[i] in h:
                    s -= nums[left]
                    h.remove(nums[left])
                    left += 1
                h.add(nums[i])
                s += nums[i]
        if len(nums) - left == k:
            mx = max(mx, s)
        return mx


if __name__ == "__main__":
    s = Solution()
    print(s.maximumSubarraySum([1, 1, 1, 7, 8, 9], 3))
