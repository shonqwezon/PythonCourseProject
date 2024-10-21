"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        d = {}
        start = 0
        mx = 0
        for i in range(len(s)):
            if s[i] in d and d[s[i]] >= start:
                mx = max(mx, i - start)
                start = d[s[i]] + 1
            d[s[i]] = i
        mx = max(mx, len(s) - start)
        return mx


if __name__ == "__main__":
    s = Solution()
    print(s.lengthOfLongestSubstring("aabbbaa"))
