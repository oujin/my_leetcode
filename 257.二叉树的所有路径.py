#
# @lc app=leetcode.cn id=257 lang=python3
#
# [257] 二叉树的所有路径
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def get_paths(root, prefix=''):
            if root is None:
                return []
            prefix = f'{prefix}->{root.val}' if prefix else str(root.val)
            if (root.left is None and root.right is None):
                return [prefix]
            return get_paths(root.left, prefix) + get_paths(root.right, prefix)
        
        return get_paths(root)
# @lc code=end

