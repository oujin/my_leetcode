#
# @lc app=leetcode.cn id=235 lang=python3
#
# [235] 二叉搜索树的最近公共祖先
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root
        while curr:
            lt1, lt2 = curr.val < p.val, curr.val < q.val
            if lt1 and lt2:
                curr = curr.right
            elif lt1 or lt2 or curr is p or curr is q:
                return curr
            else:
                curr = curr.left
        
# @lc code=end

