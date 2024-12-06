"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-substrings-that-can-be-rearranged-to-contain-a-string-i/
"""


class Solution:
    def validSubstringCount(self, word1: str, word2: str) -> int:
        left = 0
        right = 0
        d1 = {}
        d2 = {}
        k = len(word2)
        res = 0
        for i in word2:
            d2[i] = d2.get(i, 0) + 1
        while right < len(word1) and left <= right:
            d1[word1[right]] = d1.get(word1[right], 0) + 1
            if d1[word1[right]] <= d2[word1[right]]:
                k -= 1
            while left <= right and k == 0:
                res += len(word1) - right
                if d2[word1[left]] > d1[word1[left]] - 1:
                    k += 1
                d1[word1[left]] -= 1
                if d1[word1[left]] == 0:
                    del d1[word1[left]]
                left += 1
            right += 1
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.validSubstringCount("bcca", "abc"))
