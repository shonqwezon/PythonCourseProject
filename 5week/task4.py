"""
leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/linked-list-cycle-ii
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


class Solution:
    def detectCycle(self, head):
        trace = set()
        while head and head.next:
            if head not in trace:
                trace.add(head)
            else:
                return head
            head = head.next
        return None
