'''
第16章 贪心算法
    以动态规划法为基础，局部最优的策略推至全局最优，实现最优化问题求解

    16.1 活动选择问题： 调度竞争共享资源的多个活动，实现最大兼容的活动集合
        n个活动用集合S表示： S = {a1, a2, a3, ..., an}
        活动ai存在开始时间si，结束时间fi
        活动之间时间段不好重叠，即活动兼容

'''

'''
>>> 1. 递归贪心算法: 
    Recursive_Activity_Selector(s,f,k,n)
        s: 活动集合，需要按照结束时间进行预先排序
        n：活动总数
        f: 活动开始与结束时间
        k: 子问题分割节点：包含在最优解内的活动ak
        res: 存储最优解下的活动集合
'''
def Print_Result(s,f):
    result = ['a1']
    Recursive_Activity_Selector(s,f,0,len(s)-1,result)
    print(result)
    return

def Recursive_Activity_Selector(s,f,k,n,res):
    m = k+1
    while(m <= n and s[m] < f[k]):      #找到和活动ak正好衔接的活动am
        m += 1 
    if(m <= n):
        res.append('a%d' %(m+1))
        Recursive_Activity_Selector(s,f,m,n,res)
    else:
        return

'''
>>> 2. 迭代贪心算法：

'''
def Greedy_Activity_Selector(s,f):
    n = len(s)
    A = ['a1']
    k = 0
    for m in range(1, n):
        if(s[m] >= f[k]):
            A.append('a%d' %(m+1))
            k = m
    return A



S = [1,3,0,5,3,5,6,8,8,2,12]
F = [4,5,6,7,9,9,10,11,12,14,16]

Print_Result(S,F)
print(Greedy_Activity_Selector(S,F))
