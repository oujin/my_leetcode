#
# @lc app=leetcode.cn id=19 lang=python3
#
# [19] 删除链表的倒数第N个节点
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        prev, curr = head, head
        for i in range(n):
            if not curr.next and i < n - 2:
                return None
            elif not curr.next:
                return prev.next
            curr = curr.next
        while curr.next:
            prev, curr = prev.next, curr.next
        prev.next = prev.next.next
        return head
# @lc code=end

