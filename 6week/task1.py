"""
leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-number-of-nice-subarrays/
"""


class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        prefix = {0: 1}
        ans = 0
        cur_sum = 0

        for num in nums:
            cur_sum += num % 2
            target = cur_sum - k
            if target in prefix:
                ans += prefix[target]
            prefix[cur_sum] = prefix.get(cur_sum, 0) + 1

        return ans


if __name__ == "__main__":
    s = Solution()
    print(s.numberOfSubarrays([1, 1, 2, 1, 1], 3))
