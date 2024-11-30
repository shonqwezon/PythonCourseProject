"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""


class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        if len(p) > len(s):
            return []
        s_count = {}
        p_count = {}
        for i in range(len(p)):
            p_count[p[i]] = p_count.get(p[i], 0) + 1
            s_count[s[i]] = s_count.get(s[i], 0) + 1
        res = [0] if (s_count == p_count) else []
        pos = 0
        for r in range(len(p), len(s)):
            s_count[s[r]] = s_count.get(s[r], 0) + 1
            s_count[s[pos]] -= 1
            if not s_count[s[pos]]:
                s_count.pop(s[pos])
            pos += 1
            if s_count == p_count:
                res.append(pos)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.findAnagrams("cbaebabacd", "abc"))
