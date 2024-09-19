"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/word-pattern/description/
"""


class Solution:
    def reverseParentheses(self, s: str) -> str:
        stack = []
        for i, ch in enumerate(s):
            if ch == "(":
                stack.append(i)
            elif ch == ")":
                index = stack.pop()
                s = s[:index + 1] + s[i - 1:index:-1] + s[i:]
        s = s.replace("(", "").replace(")", "")
        return s


if __name__ == "__main__":
    s = Solution()
    print(s.reverseParentheses("(u(love)i)"))
