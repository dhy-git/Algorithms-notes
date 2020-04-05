'''
15.2 矩阵链乘法
    给定链乘矩阵A1 A2 A3 A4， 确定括号化方案使得计算代价最小
'''
NULL = 65535
#矩阵乘法
def Matrix_Multiply(A,B):
    r_A = len(A)
    c_A = len(A[0])
    r_B = len(B)
    c_B = len(B[0])
    if(c_A != r_B):
        print("Error: Matirx cannot multiply")
    else:
        C = [[0 for i in range(c_B)] for j in range(r_A)]   
        print(C)
        for i in range(0, r_A):
            for j in range(0, c_B):
                for k in range(c_A):
                    C[i][j] += A[i][k]*B[k][j]
    return C                

'''
    方法一： 自底向上

    Matrix_Chain_Order(p):  自底向上的最优括号化问题求解： 
            时间复杂度O(n^3) ， 空间复杂度O(n^2)。
        （原始最优括号方案的时间复杂度与n呈指数关系）
'''
def Matrix_Chain_Order(p):
    n = len(p)      # len(P) = length+1   length为矩阵链的长度
    m = [[0 for i in range(n)] for j in range(n)]   #记录A<i...j>计算次数
    print(m)
    s = [[0 for i in range(n)] for j in range(n)]   #记录构造最优解所需的信息
    for l in range(2,n):
        for i in range(1,n-l+1):
            j = i+l-1
            m[i][j] = NULL
            for k in range(i, j):
                q = m[i][k]+m[k+1][j] + p[i-1]*p[k]*p[j]
                if(q< m[i][j]): 
                    m[i][j] = q
                    s[i][j] = k
    return m,s

'''
    Print_Optimal_Parens   输出矩阵链<A1, A2, A3, ... , An> 的最优括号化方案: 
            输入Matrix_Chain_Order方法得到的信息表，以及下标i,j
            输出最优化方案
'''
def Print_Optimal_Parens(s,i,j):
    if(i == j):
        print('A%d*' %(i),end='')
    else:
        print("<",end='')
        Print_Optimal_Parens(s,i,s[i][j])
        Print_Optimal_Parens(s,s[i][j]+1,j)
        print(">",end='')
    return

P = [30,35,15,5,10,20,25]
M,S =Matrix_Chain_Order(P)
print('\n M=')
for each in M:
    print(each)
print('\n S=')
for each in S:
    print(each)
Print_Optimal_Parens(S,1,6)


'''
    方法二：带备忘的自顶向下法
'''

def Memoized_Matrix_Chain(p):
    n = len(p)
    m = [[0 for i in range(n)] for j in range(n)]   #记录A<i...j>计算次数
    for i in range(1, n):
        for j in range(i, n):
            m[i][j] = NULL
    return Lookup_Chain(m,p,1,n-1)

def Lookup_Chain(m,p,i,j):
    if(m[i][j] < NULL):
        return m[i][j]
    if(i == j):
        m[i][j] = 0
    else:
        for k in range(i,j):
            q = Lookup_Chain(m,p,i,k) + Lookup_Chain(m,p,k+1,j) + p[i-1]*p[k]*p[j]      #递推式
            if(q < m[i][j]):
                m[i][j] = q
    return m[i][j]


print(Memoized_Matrix_Chain(P))