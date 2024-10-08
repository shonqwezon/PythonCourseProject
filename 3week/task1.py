"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/container-with-most-water/
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        left = 0
        right = len(height) - 1
        max_area = 0
        cur_area = 0

        while left < right:
            cur_area = (right - left) * min(height[left], height[right])
            max_area = max(max_area, cur_area)
            if height[left] <= height[right]:
                left += 1
            elif height[left] > height[right]:
                right -= 1
        return max_area


if __name__ == "__main__":
    s = Solution()
    print(s.maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
