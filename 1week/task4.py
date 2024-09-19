"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/minimum-window-substring
"""


class Solution:
    def getDict(self, s: str):
        res = {}
        for i in s:
            if not res.get(i):
                res[i] = 0
            res[i] += 1
        return res

    def is_greater(self, d1: dict, d2: dict):
        for i in d1.keys():
            if d1[i] < d2[i]:
                return False
        return True

    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ""
        if len(s) == len(t) and set(s) != set(t):
            return ""

        MAX = len(s) + 1

        letters = self.getDict(t)
        t_letters = {}
        for k in t:
            t_letters[k] = 0

        # Init left pointer
        left, right = 0, 0
        for i, ch in enumerate(s):
            if ch in t:
                left = i
                break

        index = []
        t_letters[s[left]] = 1
        right = left
        res = (MAX, left)
        while True:
            flag = self.is_greater(t_letters, letters)
            if flag:
                res = min(res, (right - left + 1, left))
                t_letters[s[left]] -= 1
                if len(index):
                    left = index.pop(0)
                continue

            if right + 1 < len(s):
                right += 1
                ch = s[right]
                if ch in t:
                    index.append(right)
                    t_letters[ch] += 1
            else:
                break

        if sum(res) > len(s):
            return ""
        return s[res[1]:sum(res)]


if __name__ == "__main__":
    s = Solution()
    print(s.minWindow("a", "a"))
