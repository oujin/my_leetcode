#
# @lc app=leetcode.cn id=100 lang=python3
#
# [100] 相同的树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        p_list, q_list = [p], [q]
        while len(p_list) and len(q_list):
            if p_list[0] is not None and q_list[0] is None:
                return False
            if q_list[0] is not None and p_list[0] is None:
                return False
            if p_list[0] is not None and q_list[0] is not None:
                if p_list[0].val != q_list[0].val:
                    return False
                p_list.append(p_list[0].left)
                p_list.append(p_list[0].right)
                q_list.append(q_list[0].left)
                q_list.append(q_list[0].right)
            p_list, q_list = p_list[1:], q_list[1:]
        return True


# @lc code=end
