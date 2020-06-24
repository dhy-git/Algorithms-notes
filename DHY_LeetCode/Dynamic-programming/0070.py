
# [70] 爬楼梯
#

# @lc code=start
class Solution:
    def climbStairs(self, n: int) -> int:
        DP = [0 for i in range(n+1)]
        for i in range(1,n+1):
            if i == 1:
                DP[1] = 1
            elif i == 2:
                DP[2] = 2
            else:
                DP[i] = DP[i-2] + DP[i-1]
        return DP[n] 
# @lc code=end

'''
Accepted
45/45 cases passed (44 ms)
Your runtime beats 38.51 % of python3 submissions
Your memory usage beats 20.59 % of python3 submissions (13.7 MB)
'''