#
# @lc app=leetcode.cn id=232 lang=python3
#
# [232] 用栈实现队列
#

# @lc code=start
class MyQueue:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.que = []
        self.head = 0
        self.tail = 0


    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.que.append(x)
        self.tail += 1


    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        self.head += 1
        return self.que[self.head-1]


    def peek(self) -> int:
        """
        Get the front element.
        """
        return self.que[self.head]


    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return self.tail == self.head



# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()
# @lc code=end

