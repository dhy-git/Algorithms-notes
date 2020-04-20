'''
>>>柠檬水找零
Category	Difficulty	Likes	Dislikes
algorithms	Easy (54.57%)	105	-
在柠檬水摊上，每一杯柠檬水的售价为 5 美元。
顾客排队购买你的产品，（按账单 bills 支付的顺序）一次购买一杯。
每位顾客只买一杯柠檬水，然后向你付 5 美元、10 美元或 20 美元。
你必须给每个顾客正确找零，也就是说净交易是每位顾客向你支付 5 美元。
注意，一开始你手头没有任何零钱。
如果你能给每位顾客正确找零，返回 true ，否则返回 false 。

示例：
输入：[5,5,5,10,20]
输出：true
解释：
前 3 位顾客那里，我们按顺序收取 3 张 5 美元的钞票。
第 4 位顾客那里，我们收取一张 10 美元的钞票，并返还 5 美元。
第 5 位顾客那里，我们找还一张 10 美元的钞票和一张 5 美元的钞票。
由于所有客户都得到了正确的找零，所以我们输出 true。

提示：
0 <= bills.length <= 10000
bills[i] 不是 5 就是 10 或是 20 
'''

# @lc code=start
from typing import List
class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        map_dollor = {5:0,10:0,20:0}
        for each in bills:
            if each == 5:
                map_dollor[5]+=1
            elif each == 10 and map_dollor[5]>0:
                map_dollor[10]+=1
                map_dollor[5]-=1
            elif each == 20:
                if map_dollor[10]>0 and map_dollor[5]>0:
                    map_dollor[20]+=1
                    map_dollor[5]-=1
                    map_dollor[10]-=1
                elif map_dollor[5]>2:
                    map_dollor[20]+=1
                    map_dollor[5]-=3
                else:
                    return False
            else:
                return False
        return True
# @lc code=end