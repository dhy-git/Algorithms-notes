# [139] 单词拆分
#

# @lc code=start
from typing import List
class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        DP = [False for i in range(len(s)+1)]
        DP[0] = True
        for i in range(1,len(s)+1):
            for j in range(i):
                if DP[j] and s[j:i] in wordDict:
                    DP[i] = True
                    break
        return DP[-1]
# @lc code=end

'''
Accepted
36/36 cases passed (60 ms)
Your runtime beats 29.29 % of python3 submissions
Your memory usage beats 16.67 % of python3 submissions (13.8 MB)
'''