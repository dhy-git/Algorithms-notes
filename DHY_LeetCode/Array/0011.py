'''
>>>盛最多水的容器
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (59.12%)	1259	-

    给你 n 个非负整数 a1，a2，...，an，每个数代表坐标中的一个点 (i, ai) 。
    在坐标内画 n 条垂直线，垂直线 i 的两个端点分别为 (i, ai) 和 (i, 0)。
    找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。
    说明：你不能倾斜容器，且 n 的值至少为 2。

    示例：
    输入：[1,8,6,2,5,4,8,3,7]
    输出：49
'''
from typing import List
''' 
 注： 动态规划 算法时间复杂度O(n)
'''

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maximum = 0
        i = 0
        j = len(height) - 1
        while(j > i):
            maximum = max((j-i)*min(height[i],height[j]), maximum)
            if(height[i]<height[j]):
                i += 1
            else:
                j -= 1
        return maximum
# @lc code=end



'''
Accepted
50/50 cases passed (80 ms)
Your runtime beats 68.33 % of python3 submissions
Your memory usage beats 5 % of python3 submissions (15.1 MB)
'''