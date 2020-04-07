'''
>>>买卖股票的最佳时机
    Category	Difficulty	Likes	Dislikes
    algorithms	Easy (51.31%)	881	-
    给定一个数组，它的第 i 个元素是一支给定股票第 i 天的价格。
    如果你最多只允许完成一笔交易（即买入和卖出一支股票一次），设计一个算法来计算你所能获取的最大利润。
    注意：你不能在买入股票前卖出股票。

    示例 1:
    输入: [7,1,5,3,6,4]
    输出: 5
    解释: 在第 2 天（股票价格 = 1）的时候买入，在第 5 天（股票价格 = 6）的时候卖出，最大利润 = 6-1 = 5 。
        注意利润不能是 7-1 = 6, 因为卖出价格需要大于买入价格。
    示例 2:
    输入: [7,6,4,3,1]
    输出: 0
    解释: 在这种情况下, 没有交易完成, 所以最大利润为 0。
'''
# @lc code=start
from typing import List
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        if(n == 0):
            return 0
        tmp = [0 for i in range(n)]
        min_price = prices[0]
        for i in range(1,n):
            min_price = min(min_price, prices[i])
            tmp[i] = max(tmp[i-1],prices[i]- min_price)
        return tmp[n-1]
# @lc code=end

'''
200/200 cases passed (60 ms)s
Your runtime beats 54.94 % of python3 submissions
Your memory usage beats 6.51 % of python3 submissions (14.4 MB)
'''