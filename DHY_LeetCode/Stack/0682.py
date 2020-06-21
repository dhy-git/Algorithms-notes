
# [682] 棒球比赛
#

# @lc code=start
from typing import List
class Solution:
    def calPoints(self, ops: List[str]) -> int:
        s = []
        for each in ops:
            if isnum(each):
                s.append(int(each))
            elif each == 'C':
                s.pop()
            elif each == '+':
                s.append(s[-1]+s[-2])
            elif each == 'D':
                s.append(s[-1]*2)
        return sum(s)
        
def isnum(s) -> int:
    try:
        n = int(s)
        return True
    except ValueError:
        return False


# @lc code=end

'''
Accepted
39/39 cases passed (72 ms)
Your runtime beats 12.08 % of python3 submissions
Your memory usage beats 14.29 % of python3 submissions (13.7 MB)
'''