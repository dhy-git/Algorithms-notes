# [150] 逆波兰表达式求值
#

# @lc code=start
from typing import List
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        num_stack = []
        for each in tokens:
            if each=='+':
                num_stack.append(num_stack.pop()+num_stack.pop())
            elif each=='-':
                tmp = num_stack.pop()
                num_stack.append(num_stack.pop()-tmp)
            elif each=='*':
                num_stack.append(num_stack.pop() * num_stack.pop())
            elif each=='/':
                tmp = num_stack.pop()
                num_stack.append(int(num_stack.pop()/tmp))
            else:
                num_stack.append(int(each))
        return num_stack[0]

# @lc code=end

'''
Accepted
20/20 cases passed (52 ms)
Your runtime beats 54.31 % of python3 submissions
Your memory usage beats 12.5 % of python3 submissions (14 MB)
'''

