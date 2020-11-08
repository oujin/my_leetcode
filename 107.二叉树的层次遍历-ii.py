#
# @lc app=leetcode.cn id=107 lang=python3
#
# [107] 二叉树的层次遍历 II
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        if root is None:
            return []
        layers, values = [[root]], [[root.val]]
        while layers[-1]:
            next_layer, next_val = [], []
            for node in layers[-1]:
                if node.left is not None:
                    next_layer.append(node.left)
                    next_val.append(node.left.val)
                if node.right is not None:
                    next_layer.append(node.right)
                    next_val.append(node.right.val)
            layers.append(next_layer)
            values.append(next_val)
        return values[:-1][::-1]

# @lc code=end

