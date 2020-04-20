'''
>>>三维形体的表面积
    Category	Difficulty	Likes	Dislikes
    algorithms	Easy (64.25%)	107	-
    在 N * N 的网格上，我们放置一些 1 * 1 * 1  的立方体。

    每个值 v = grid[i][j] 表示 v 个正方体叠放在对应单元格 (i, j) 上。
    请你返回最终形体的表面积。

    
    输入：[[2,2,2],[2,1,2],[2,2,2]]
    输出：46
    
    提示：
    1 <= N <= 50
    0 <= grid[i][j] <= 50

'''
# @lc code=start
from typing import List
class Solution:
    def surfaceArea(self, grid: List[List[int]]) -> int:
        top = 0
        left = [0 for row in range(len(grid)+1)]
        front = [0 for column in range(len(grid[0])+1)]

        count = [[0 for column in range(len(grid[0])+2)] for row in range(len(grid)+2)]
        for i in range(1,len(grid)+2):
            for j in range(1,len(grid[0])+2):
                #边界条件
                if i<(len(grid)+1) and j<(len(grid[0])+1):
                    count[i][j] = grid[i-1][j-1]
                    if grid[i-1][j-1]>0:
                        top+=1
                front[j-1]+= abs(count[i][j]-count[i-1][j])
                left[i-1]+= abs(count[i][j]-count[i][j-1])
        return top*2+sum(left)+sum(front)
# @lc code=end

'''
Accepted
90/90 cases passed (184 ms)
Your runtime beats 18.75 % of python3 submissions
Your memory usage beats 33.33 % of python3 submi
'''