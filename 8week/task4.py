"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/take-k-of-each-character-from-left-and-right/description
"""


class Solution:
    def takeCharacters(self, s: str, k: int) -> int:
        count = [0, 0, 0]
        for c in s:
            count[ord(c) - ord("a")] += 1

        if min(count) < k:
            return -1

        res = 10**10
        left = 0
        for right in range(len(s)):
            count[ord(s[right]) - ord("a")] -= 1

            while min(count) < k:
                count[ord(s[left]) - ord("a")] += 1
                left += 1
            res = min(res, len(s) - (right - left + 1))
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.takeCharacters("aabaaaacaabc", 2))
