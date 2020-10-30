#
# @lc app=leetcode.cn id=101 lang=python3
#
# [101] 对称二叉树
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root is None:
            return True
        curr_layer, next_layer = [root], []
        while curr_layer:
            for i in range(len(curr_layer) // 2):
                if curr_layer[i] is None and curr_layer[-i-1] is None:
                    continue
                if curr_layer[i] is None and curr_layer[-i-1] is not None:
                    return False
                if curr_layer[-i-1] is None and curr_layer[i] is not None:
                    return False
                if curr_layer[i].val != curr_layer[-i-1].val:
                    return False
            for n in curr_layer:
                if n is not None:
                    next_layer.append(n.left)
                    next_layer.append(n.right)
            curr_layer, next_layer = next_layer, []
        return True
        
# @lc code=end

