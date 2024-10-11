"""
leetcode.com/problem-list/prefix-sum/
url: https://leetcode.com/problems/product-of-array-except-self/
"""


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        prefix = [1]
        suffix = [1]
        for i in nums:
            prefix.append(prefix[-1] * i)
        for i in nums[::-1]:
            suffix.append(suffix[-1] * i)

        ans = [0] * len(nums)
        for i in range(len(nums)):
            ans[i] = suffix[len(suffix) - i - 2] * prefix[i]
        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.productExceptSelf([1, 2, 3, 4]))
