"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-repeating-character-replacement/
"""


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        for ch in range(ord("A"), ord("Z") + 1):
            ch = chr(ch)
            i, j, r = 0, 0, 0
            while j < len(s):
                if s[j] == ch:
                    j += 1
                elif r < k:
                    j += 1
                    r += 1
                elif s[i] == ch:
                    i += 1
                else:
                    i += 1
                    r -= 1
                res = max(j - i, res)
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.characterReplacement("ABAB", 2))
