"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum
"""


class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        nums.sort()

        res = []
        l_nums = len(nums)
        for i in range(l_nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            target = -nums[i]
            j = i + 1
            k = l_nums - 1
            while j < k:
                if nums[j] + nums[k] > target:
                    k -= 1
                elif nums[j] + nums[k] < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
                    while j < k and nums[j] == nums[j - 1]:
                        j += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSum([0, 0, 0, 0]))
