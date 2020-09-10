# [155] 最小栈
#

# @lc code=start
class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.ministack = []
        self.mininum = []


    def push(self, x: int) -> None:
        self.ministack.append(x)
        if (len(self.mininum) ==0) or (self.mininum[-1]>=x):
            self.mininum.append(x)

    def pop(self) -> None:
        if len(self.mininum) >0 and (self.mininum[-1] == self.ministack[-1]):
            self.mininum.pop(-1)
        self.ministack.pop(-1)

    def top(self) -> int:
        return self.ministack[-1]

    def getMin(self) -> int:
        return self.mininum[-1]



# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(x)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
# @lc code=end

