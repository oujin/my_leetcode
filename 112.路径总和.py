#
# @lc app=leetcode.cn id=112 lang=python3
#
# [112] 路径总和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if root is None:
            return False
        layers, cnts = [[root]], [[0]]
        while layers[-1]:
            layer, cnt = [], []
            for i, node in enumerate(layers[-1]):
                if cnts[-1][i] + node.val == sum:
                    if node.left is None and node.right is None:
                        return True
                if node.left is not None:
                    layer.append(node.left)
                    cnt.append(cnts[-1][i] + node.val)
                if node.right is not None:
                    layer.append(node.right)
                    cnt.append(cnts[-1][i] + node.val)
            layers.append(layer)
            cnts.append(cnt)
        return False


# @lc code=end

