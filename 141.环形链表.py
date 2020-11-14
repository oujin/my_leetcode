#
# @lc app=leetcode.cn id=141 lang=python3
#
# [141] 环形链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        if head is None:
            return False
        p1 = p2 = head
        while True:
            for _ in range(2):
                if p2.next is not None:
                    p2 = p2.next
                else:
                    return False
            p1 = p1.next
            if p1 == p2:
                return True
        
# @lc code=end

