#
# @lc app=leetcode.cn id=110 lang=python3
#
# [110] 平衡二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalancedAndCount(self, root):
        if root is None:
            return True, 0
        leftIsBalanced, left_n = self.isBalancedAndCount(root.left)
        if not leftIsBalanced:
            return False, -1
        rightIsBalanced, right_n = self.isBalancedAndCount(root.right)
        if not rightIsBalanced:
            return False, -1
        if abs(left_n - right_n) > 1:
            return False, -1
        return True, max(left_n, right_n) + 1

    def isBalanced(self, root: TreeNode) -> bool:
        isBal, _ = self.isBalancedAndCount(root)
        return isBal
        
# @lc code=end

