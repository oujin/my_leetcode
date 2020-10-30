#
# @lc app=leetcode.cn id=104 lang=python3
#
# [104] 二叉树的最大深度
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        depth = 0
        if root is None:
            return depth
        curr_layer, next_layer = [root], []
        while curr_layer:
            depth += 1
            for n in curr_layer:
                if n.left is not None:
                    next_layer.append(n.left)
                if n.right is not None:
                    next_layer.append(n.right)
            curr_layer, next_layer = next_layer, []
        return depth
        
# @lc code=end

