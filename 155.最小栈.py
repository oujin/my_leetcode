#
# @lc app=leetcode.cn id=155 lang=python3
#
# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.n_min = []
        self.stack = []

    def push(self, x: int) -> None:
        self.stack.append(x)
        if len(self.n_min):
            self.n_min.append(min(self.n_min[-1], x))
        else:
            self.n_min.append(x)


    def pop(self) -> None:
        self.stack = self.stack[:-1]
        self.n_min = self.n_min[:-1]

    def top(self) -> int:
        return self.stack[-1]


    def getMin(self) -> int:
        return self.n_min[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

