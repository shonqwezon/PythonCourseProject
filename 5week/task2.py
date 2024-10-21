"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/group-anagrams
"""


class Solution:
    def groupAnagrams(self, strs: list[str]) -> list[list[str]]:
        d = {}
        for i in strs:
            b = "".join(sorted(i))
            if b not in d:
                d[b] = []
            d[b].append(i)

        return list(d.values())


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["ddddddddddg", "dgggggggggg"]))
