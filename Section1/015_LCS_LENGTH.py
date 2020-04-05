'''
15.4 最长公共子序列问题
    给定序列     X = {x1, x2, ..., xm}
                Y = {y1, y2, ..., yn}
    求 X、Y的最长公共自序列Z
        定义 Xi为X的前i个元素组成的子序列
'''

def LCS_Length(X,Y):
    m = len(X)
    n = len(Y)
    b = [[0 for column in range(n+1)] for row in range(m+1)]
    c = [[0 for column in range(n+1)] for row in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if(X[i-1] == Y[j-1]):
                c[i][j] = c[i-1][j-1]+1 
                b[i][j] = 'G'
            elif(c[i-1][j] >= c[i][j-1]):
                c[i][j] = c[i-1][j]
                b[i][j] = 'X'
            else:
                c[i][j] = c[i][j-1]
                b[i][j] = 'Y'
    return b,c

#打印最长公共子序列
def Print_LCS(b, X, i, j):
    if(i == 0 or j == 0):
        return 
    if(b[i][j] == "G"):
        Print_LCS(b, X, i-1, j-1)
        print(X[i-1], end='')
    elif(b[i][j] == "X"):
        Print_LCS(b, X, i-1, j)
    else:
        Print_LCS(b, X, i, j-1) 

#测试代码：
X = 'ABCBDAB'
Y = 'BDCABA'

b,c = LCS_Length(X,Y)
for row in b:
    print(row)
Print_LCS(b,X,len(X), len(Y))