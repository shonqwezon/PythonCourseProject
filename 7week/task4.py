"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-of-substrings-containing-every-vowel-and-k-cons-i
"""


class Solution:

    def countOfSubstrings(self, word: str, k: int) -> int:
        res = 0
        for i in range(len(word)):
            vset = set("aeiou")
            cons = 0

            for j in range(i, len(word)):
                if word[j] in "aeiou":
                    vset.discard(word[j])
                else:
                    cons += 1
                if cons == k and not len(vset):
                    res += 1
                if cons > k:
                    break
        return res


if __name__ == "__main__":
    s = Solution()
    print(s.countOfSubstrings("aeioqq", 1))
