#
# @lc app=leetcode.cn id=206 lang=python3
#
# [206] 反转链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if head is None or head.next is None:
            return head
        # # 迭代
        # pre, curr = head, head.next
        # head.next = None
        # while curr:
        #     tmp = curr.next    
        #     curr.next = pre
        #     pre, curr = curr, tmp
        # return pre
        
        # 递归
        tail = head
        while tail.next.next:
            tail = tail.next
        new_head = tail.next
        tail.next = None
        new_head.next = self.reverseList(head)
        return new_head


# @lc code=end

