#
# @lc app=leetcode.cn id=160 lang=python3
#
# [160] 相交链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return None
        p1, p2 = headA, headB
        n1, n2 = 0, 0
        while p1.next:
            n1 += 1
            p1 = p1.next
        while p2.next:
            n2 += 1
            p2 = p2.next
        if p1 != p2:
            return None
        p1, p2 = headA, headB
        if n1 < n2:
            for _ in range(n2 - n1):
                p2 = p2.next
        if n2 < n1:
            for _ in range(n1 - n2):
                p1 = p1.next
        while p1 and p2:
            if p1 == p2:
                return p1
            p1, p2 = p1.next, p2.next
        return None
            

# @lc code=end

