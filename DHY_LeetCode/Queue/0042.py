'''
接雨水
Category	Difficulty	Likes	Dislikes
algorithms	Hard (50.59%)	1216	-
给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。
上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 感谢 Marcos 贡献此图。

示例:
输入: [0,1,0,2,1,0,1,3,2,1,2,1]
输出: 6
'''

# @lc code=start
from typing import List 
class Solution:
    def trap(self, height: List[int]) -> int:
        save = 0
        stack_trap = [0]
        for i in range(1,len(height)):
            #非单调递减，迭代累计save
            while height[i] >= height[stack_trap[-1]]:
                tmp = stack_trap.pop()
                if len(stack_trap) > 0:
                    save += (min(height[stack_trap[-1]],height[i]) - height[tmp])*(i-stack_trap[-1]-1)
                    #print('stack pop',tmp,'save water',save)
                else:
                    #print('eage warning')
                    break
            #单调递减 入栈
            stack_trap.append(i)
            #print('stack stright push',i)
        return save
# @lc code=end

'''
Accepted
315/315 cases passed (44 ms)
Your runtime beats 87.95 % of python3 submissions
Your memory usage beats 8 % of python3 submissions (14.2 MB)
'''
