"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/alternating-groups-i/description
"""


class Solution:
    def numberOfAlternatingGroups(self, colors: list[int]) -> int:
        res = 0
        for i in range(-1, len(colors) - 1):
            if colors[i + 1] != colors[i] and colors[i - 1] == colors[i + 1]:
                res += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfAlternatingGroups([1, 1, 1]))
