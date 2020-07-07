'''
    二叉搜索树性质 root.left.val < root.val < root.right.val
    解法1 动态规划
    解法2 等效 -- 【卡塔兰数】序列表达式
'''
# [96] 不同的二叉搜索树
#

# @lc code=start
class Solution:
    def numTrees(self, n: int) -> int:
        DP = [0 for i in range(n+1)]
        DP[0] = 1
        DP[1] = 1 
        for i in range(2,n+1):
            for j in range(1,i+1):
                DP[i] += DP[j-1]*DP[i-j]
        print( DP)
        return DP[n]
# @lc code=end


sol = Solution()
sol.numTrees(5)
'''
Accepted
19/19 cases passed (36 ms)
Your runtime beats 84.31 % of python3 submissions
Your memory usage beats 5.26 % of python3 submissions (13.7 MB)
'''