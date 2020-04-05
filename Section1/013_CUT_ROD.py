'''
    第15章 动态规划
        动态规划法解决最优化问题，需要具备的两个要素：
            >最优子结构————递归
            >子问题重叠————空间换时间
        一般方法：
            1.刻画最优解的结构特征
            2.递归定义最优解的值
            3.计算最优解的值，通常使用自底向上的方法
            4. 利用计算的信息构造最优解

    15.1钢条切割问题
    长度i   1   2   3   4   5   6   7   8   9   10
    价格pi  1   5   8   9   10  17  17  20  24  30  

    求解长度为n 的钢条切割最大收益
'''

NULL = -65535
#盈利表
P = [0, 1, 5, 8, 9, 10, 17, 17, 20, 24, 30]

'''
>>> 1. 递归实现：
        遍历所有切割方法，返回最大盈利值，运行时间为n的 指数函数
'''
def Cut_Rod(p, n):
    if n == 0:
        return 0
    q =  NULL
    for i in range(1,n+1):
        if(i < len(p)):
            q = max(q, p[i]+Cut_Rod(p,n-i))
    return q

#测试自顶向下递归代码：
import time
start = time.perf_counter()
end = time.perf_counter()
#print('max value:', Cut_Rod(P, 2))
#print('运行耗时：%.5fus' %((end- start)*1000000))


'''
>>> 2 动态规划方法一： 带备忘的自顶向下法
        r[n] 记录长度为n的钢条盈利最大的分解方案，以空间换时间，运行时间是n的多项式阶次
'''
def Memoized_Cut_Rod(p,n):
    r = [NULL for i in range(n+1)]
    return Memoized_Cut_Rod_Aux(p,n,r)

def Memoized_Cut_Rod_Aux(p, n, r):
    if(r[n] >= 0):
        return r[n]
    if(n == 0):
        q = 0
    else:
        q = NULL
        for i in range(1,n+1):
            if(i < len(p)):
                q = max(q, p[i]+ Memoized_Cut_Rod_Aux(p, n-i, r))
    r[n] = q
    return q

#print('max value:', Memoized_Cut_Rod(P, 70))
#print('运行耗时：%.5fus' %((end- start)*1000000))


'''
>>> 3动态规划方法二： 自底而上法
    

'''

def Bottom_Cut_Rod(p,n):
    r = [0 for i in range(0,n+1)]
    for j in range(1,n+1):
        q = NULL
        for i in range(1,j+1):
            if(i < len(p)):
                q = max(q, p[i]+r[j-i])
        r[j] = q
    return r[n]

#print('max value:', Bottom_Cut_Rod(P, 70))
#print('运行耗时：%.5fus' %((end- start)*1000000))


'''
>>> 4 重构解：给出上述动态规划算法在最大盈利下的最优解和收益值
'''

def Extended_Bottom_Cut_Rod(p,n):
    r = [0 for i in range(0,n+1)]   #保存s[n]保存长度n时的最大收益
    s = [0 for i in range(0,n+1)]   #保存长度为n的钢条最佳处理方案下第一段的截取长度，剩余截取长度通过查询s[i]递推即可
    for j in range(1,n+1):
        q = NULL
        for i in range(1,j+1):
            if(i < len(p) and q< p[i]+r[j-i]):
                q = p[i]+r[j-i]
                s[j] = i
                r[j] = q
    return r,s

def Print_Cut_Rod_Solution(p,n):
    count = 0
    r,s = Extended_Bottom_Cut_Rod(p,n)
    print('maximum profile is %.2f' %(r[n]))
    while(n>0):
        count +=1
        print('第%d段长度：%.1f' %(count,s[n]))
        n = n - s[n]

Print_Cut_Rod_Solution(P,13)
