#
# @lc app=leetcode.cn id=2 lang=python3
#
# [2] 两数相加
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        s = l1.val + l2.val
        c = s // 10
        head = ListNode(s % 10)
        new_l = head
        l1, l2 = l1.next, l2.next
        while l1 is not None and l2 is not None:
            s = l1.val + l2.val + c
            c = s // 10
            new_l.next = ListNode(s % 10)
            new_l = new_l.next
            l1, l2 = l1.next, l2.next
        if l1 is None and l2 is None:
            new_l.next = None if c == 0 else ListNode(c)
        else:
            l3 = l1 if l2 is None else l2
            while l3 is not None:
                s = l3.val + c
                c = s // 10
                new_l.next = ListNode(s % 10)
                new_l, l3 = new_l.next, l3.next
                if c == 0:
                    new_l.next = l3
                    break
            if c > 0:
                new_l.next = ListNode(c)
        return head   

# @lc code=end

