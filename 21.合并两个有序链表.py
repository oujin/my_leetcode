#
# @lc app=leetcode.cn id=21 lang=python3
#
# [21] 合并两个有序链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        if l1 is None or l2 is None:
            return l2 if l1 is None else l1
        if l1.val < l2.val:
            return ListNode(l1.val, self.mergeTwoLists(l1.next, l2))
        return ListNode(l2.val, self.mergeTwoLists(l1, l2.next))
        
# @lc code=end

