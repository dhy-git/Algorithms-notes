'''
现金支付问题：1、2、5元零钱遍历所有支付方法 
递归方法实现（优化排除重复情况）
'''
from typing import List
class Solution:
    def __init__(self):
        self.sol = []
    
    def pay(self, m:int):
        st = []
        self.search(m,st)
        for each in self.sol:
            print(each)

    def search(self, m: int, s:List[int]) -> List[int]:
        money = [1,2,5]
        for each in money:
            way = s[:]
            tmp = m - each
            way.append(each)
            if (tmp) == 0:
                #print(way)
                #去重优化
                way = sorted(way)
                if way not in self.sol:
                    self.sol.append(way)
            elif (tmp) > 0:
                
                self.search(tmp, way)



sol = Solution()
sol.pay(5)
