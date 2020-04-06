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


#本地编译加入模块
from typing import List
import sys

#LeetCode 提交代码：
# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        m = len(nums1)
        n = len(nums2)
        return (self.find_index_x(nums1, nums2, 0, 0, int((m+n+1)/2)) + self.find_index_x(nums1, nums2, 0, 0, int((m+n+2)/2)))/2

    '''
    功能： 递归实现寻找有序数组A[i]~A[n]、B[j]~B[m]中第x小的数，并返回其下标
    '''
    def find_index_x(self, A, B, i, j, x):
        #边界条件
        if(i > len(A)-1):
            return B[j+x-1]
        if(j > len(B)-1):
            return A[i+x-1]
        if(x == 1):
            return (min(A[i],B[j]))
        
        #递归
        val_midA = A[i+int(x/2)-1] if(i+int(x/2)-1 < len(A))  else sys.maxsize
        val_midB = B[j+int(x/2)-1] if(j+int(x/2)-1 < len(B))  else sys.maxsize
        if( val_midA < val_midB):
            #print("cutA  %d %d"%(i, j))
            return self.find_index_x(A,B, i+int(x/2), j, x-int(x/2))
        else:
            #print("cutB  %d %d"%(i, j))
            return self.find_index_x(A,B, i, j+int(x/2), x-int(x/2))
# @lc code=end

#本地测试代码：
nums1 = [10, 20, 30, 40]
nums2 = [50, 60, 70, 80]
sol = Solution()
ans = sol.findMedianSortedArrays(nums1, nums2)
print(ans)


'''
Accepted
2085/2085 cases passed (84 ms)
Your runtime beats 55.49 % of python3 submissions
Your memory usage beats 5.61 % of python3 submissions (13.8 MB)
'''