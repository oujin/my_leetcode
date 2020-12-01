#
# @lc app=leetcode.cn id=404 lang=python3
#
# [404] 左叶子之和
#

# @lc code=start
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:
        n = 0
        if not root:
            return n

        def isLeaf(root):
            return (not root.left) and (not root.right)

        nodes, i = [root], 0
        while i < len(nodes):
            if nodes[i].left:
                if isLeaf(nodes[i].left):
                    n += nodes[i].left.val
                else:
                    nodes.append(nodes[i].left)
            if nodes[i].right:
                if not isLeaf(nodes[i].right):
                    nodes.append(nodes[i].right)
            i += 1
        return n


# @lc code=end

