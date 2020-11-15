class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if headA is None or headB is None:
            return False
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
     

n0 = ListNode(4)
n1 = ListNode(1)
n2 = ListNode(8)
n3 = ListNode(4)
n4 = ListNode(5)
n5 = ListNode(5)
n6 = ListNode(6)
n7 = ListNode(1)
n0.next = n1
n1.next = n2
n2.next = n3
n3.next = n4
n5.next = n6
n6.next = n7
n7.next = n2
s = Solution()
node = s.getIntersectionNode(n0, n5)
# print(node, n5)
print(node.val)