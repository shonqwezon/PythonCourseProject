"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-consonants-ii
"""


class Solution:

    def func(self, s, k):
        i, j, count, vows, ans = 0, 0, [0] * 6, "aeiou", 0
        for j, ch in enumerate(s):
            if ch in vows:
                count[vows.find(ch)] += 1
            else:
                count[-1] += 1
            while all(count[p] > 0 for p in range(5)) and count[-1] >= k:
                ans += len(s) - j
                if s[i] in vows:
                    count[vows.find(s[i])] -= 1
                else:
                    count[-1] -= 1
                i += 1
        return ans

    def countOfSubstrings(self, word: str, k: int) -> int:
        return self.func(word, k) - self.func(word, k + 1)


if __name__ == "__main__":
    s = Solution()
    print(s.countOfSubstrings("aeioqq", 1))
