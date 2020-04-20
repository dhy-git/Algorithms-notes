'''
>>>矩形区域不超过 K 的最大数值和
    Category	Difficulty	Likes	Dislikes
    algorithms	Hard (32.08%)	71	-
    给定一个非空二维矩阵 matrix 和一个整数 k，找到这个矩阵内部不大于 k 的最大矩形和。

    示例:
    输入: matrix = [[1,0,1],[0,-2,3]], k = 2
    输出: 2 
    解释: 矩形区域 [[0, 1], [-2, 3]] 的数值和是 2，且 2 是不超过 k 的最大数字（k = 2）。
    说明：
    矩阵内的矩形区域面积必须大于 0。
    如果行数远大于列数，你将如何解答呢？
'''

# @lc code=start

'''
    解1：动态规划方法
未通过
'''
from typing import List
class Solution1:
    def maxSumSubmatrix(self, matrix: List[List[int]], k: int) -> int:
        #动态规划 DP[i][j] = DP[i-1][j] + DP[i][j-1] + matrix[i][j] - DP[i-1][j-1]
        row = len(matrix)
        column = len(matrix[0])
        DP = [[0 for i in range(column+1)] for i in range(row+1)]  
        #空间换时间 求过渡矩阵DP
        for i in range(1, row+1):
            for j in range(1, column+1):
                DP[i][j] = DP[i-1][j]+ DP[i][j-1]+ matrix[i-1][j-1]- DP[i-1][j-1]
        #print(DP)
        # 矩阵[i][j]-->[m][n] 的矩阵元素和

        max_sum =matrix[0][0]
        for i in matrix:
            for j in i:
                max_sum = min(j,max_sum)

        #data=open("D:\data.txt",'w+')       #测试行1

        for i in range(0, row):
            for j in range(0, column):
                for m in range(i+1, row+1):
                    for n in range(j+1, column+1):
                        matrix_sum =  DP[m][n] - DP[m][j]- DP[i][n]+ DP[i][j]   
                        #测试行2
                        #print('(%d,%d)-->(%d,%d) sum=%d' %(i,j,m,n,matrix_sum), file= data)

                        if(matrix_sum <= k):
                            max_sum = max(matrix_sum, max_sum)
        #data.close()       #测试行3
        return max_sum                 

#未通过case 原因未找到
A = [[27,5,-20,-9,1,26,1,12,7,-4,8,7,-1,5,8],[16,28,8,3,16,28,-10,-7,-5,-13,7,9,20,-9,26],[24,-14,20,23,25,-16,-15,8,8,-6,-14,-6,12,-19,-13],[28,13,-17,20,-3,-18,12,5,1,25,25,-14,22,17,12],[7,29,-12,5,-5,26,-5,10,-5,24,-9,-19,20,0,18],[-7,-11,-8,12,19,18,-15,17,7,-1,-11,-10,-1,25,17],[-3,-20,-20,-7,14,-12,22,1,-9,11,14,-16,-5,-12,14],[-20,-4,-17,3,3,-18,22,-13,-1,16,-11,29,17,-2,22],[23,-15,24,26,28,-13,10,18,-6,29,27,-19,-19,-8,0],[5,9,23,11,-4,-20,18,29,-6,-4,-11,21,-6,24,12],[13,16,0,-20,22,21,26,-3,15,14,26,17,19,20,-5],[15,1,22,-6,1,-9,0,21,12,27,5,8,8,18,-1],[15,29,13,6,-11,7,-6,27,22,18,22,-3,-9,20,14],[26,-6,12,-10,0,26,10,1,11,-10,-16,-18,29,8,-8],[-19,14,15,18,-10,24,-9,-7,-19,-14,23,23,17,-5,6]]
k = -100
sol = Solution1()
maxi = sol.maxSumSubmatrix(A,k)
print(maxi)
    #def sum_matrix(self, matrix: List[List[int]])

'''
    解2： 剪枝
'''


# @lc code=end

