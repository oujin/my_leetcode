#
# @lc app=leetcode.cn id=234 lang=python3
#
# [234] 回文链表
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        if head is None or head.next is None:
            return True
        slow, fast = head.next, head.next.next
        head.next = None
        head1, head2 = head, slow
        while fast and fast.next:
            head2 = slow.next
            slow.next = head1
            head1 = slow
            slow = head2
            fast = fast.next.next
        if fast is not None:
            head2 = head2.next
        while head1 and head2:
            if head1.val != head2.val:
                return False
            head1, head2 = head1.next, head2.next
        return head1 is None and head2 is None

# @lc code=end

