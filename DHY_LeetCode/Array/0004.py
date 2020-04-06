'''
>>>寻找两个有序数组的中位数
    Category	Difficulty	Likes	Dislikes
    algorithms	Hard (36.30%)	2388	-

    给定两个大小为 m 和 n 的有序数组 nums1 和 nums2。
    请你找出这两个有序数组的中位数，并且要求算法的时间复杂度为 O(log(m + n))。
    你可以假设 nums1 和 nums2 不会同时为空。

    示例 1:
    nums1 = [1, 3]
    nums2 = [2]

    则中位数是 2.0
    示例 2:

    nums1 = [1, 2]
    nums2 = [3, 4]

    则中位数是 (2 + 3)/2 = 2.5

    注：时间复杂度要求：分治算法

'''

'''
功能： 递归实现寻找有序数组A[i]~A[n]、B[j]~B[m]中第x小的数，并返回其下标
'''
#本地编译加入 Python3 类型注释模块
from typing import List

#LeetCode 提交代码：
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        return (self.find_index_x(nums1, nums2, 0, 0, int((m+n+1)/2)) + self.find_index_x(nums1, nums2, 0, 0, int((m+n+2)/2)))/2

    def find_index_x(self, A, B, i, j, x):
        #边界条件
        if(i > len(A)-1):
            return B[j+x-1]
        if(j > len(B)-1):
            return A[i+x-1]
        if(x == 1):
            return (min(A[i],B[j]))
        
        #递归
        index_midA = i+int(x/2)-1
        index_midB = j+int(x/2)-1
        new_x = x - int(x/2)
        if(A[index_midA] < B[index_midB]):
            #print("cutA  %d %d"%(i, j))
            return self.find_index_x(A,B,index_midA+1,j,new_x)
        else:
            #print("cutB  %d %d"%(i, j))
            return self.find_index_x(A,B,i,index_midB+1,new_x)

#本地测试代码：
nums1 = [10, 20, 30, 40]
nums2 = [50, 60, 70, 80]
sol = Solution()
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)