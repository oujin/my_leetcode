#
# @lc app=leetcode.cn id=61 lang=python3
#
# [61] 旋转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: ListNode, k: int) -> ListNode:
        if not head:
            return head
        length = 0
        prev = curr = head
        while curr:
            curr, length = curr.next, length + 1
        k, curr = k % length, head
        while k > 0:
            k, curr = k - 1, curr.next
        while curr.next:
            prev, curr = prev.next, curr.next
        new_head = head
        if prev.next:
            new_head = prev.next
            curr.next = head
            prev.next = None
        return new_head
# @lc code=end

