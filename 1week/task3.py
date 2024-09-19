"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/determine-if-two-strings-are-close
"""


class Solution:
    def getDict(self, s: str):
        res = {}
        for i in s:
            if not res.get(i):
                res[i] = 0
            res[i] += 1
        return sorted(res.values())

    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1) != len(word2):
            return False
        if set(word1) != set(word2):
            return False
        if self.getDict(word1) != self.getDict(word2):
            return False
        return True


if __name__ == "__main__":
    s = Solution()
    s.closeStrings("abbzzca", "babzzcz")
