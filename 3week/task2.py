"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/3sum-closest
"""


class Solution:
    def threeSumClosest(self, nums: list[int], target: int) -> int:
        nums.sort()

        res = sum(nums)
        l_nums = len(nums)
        closest = 10000
        for i in range(l_nums):
            if i > 0 and nums[i] == nums[i - 1]:
                continue
            j = i + 1
            k = l_nums - 1
            while j < k:
                s = nums[i] + nums[j] + nums[k]
                if abs(target - s) < closest:
                    res = s
                    closest = abs(target - s)
                if s > target:
                    k -= 1
                elif s < target:
                    j += 1
                else:
                    return s
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.threeSumClosest([1, 1, 1, 0], -100))
