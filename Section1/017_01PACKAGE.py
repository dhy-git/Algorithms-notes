'''
    16.2 0-1背包问题 （动态规划问题）
        相比较：分数背包为题（贪心算法）
         
        给定一组物品，每种物品都有自己的重量和价格，
        在限定的总重量内，我们如何选择，才能使得物品的总价格最高。
        
        算法：
            定义物品的重量序列w、价值序列v，背包最大容量Wmax， 定义矩阵c(n * Wmax)， c[i][w]表示对前i个物品考虑，背包总重为w时的最大价值为c[i][w]

            矩阵元素c[i][w] 赋值的几种情况 
                1> 没有物品或者质量为0，价值为0
                2> 在矩阵上一行计算结果基础上，在所有物品中遍历，若新增该物品后总重大于Wmax， 则背包总价值不变，集成同列上一行值
                3> 剩余情况，在遍历一遍物品后找到最大总价值并记录
'''

def Package_0_1(W,V,Wmax):
    n = len(W)
    c = [[0 for w in range(Wmax+1)] for i in range(n+1)]
    for i in range(1,n+1):
        for w in range(1,Wmax+1):
            if(w < W[i-1] ):
                c[i][w] = c[i-1][w]
            else:
                c[i][w] = max(c[i-1][w-W[i-1]]+V[i-1], c[i-1][w])
    return c

"""
测试数据：
"""

Max = 10 #书包能承受的重量，
Weight = [2, 2, 3, 1, 5, 2] #每个物品的重量，
Value =  [2, 3, 1, 5, 4, 3] #每个物品的价值

C = Package_0_1(Weight,Value,Max)
for row in C:
    print(row)