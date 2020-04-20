'''
>>>最大子序和
    Category	Difficulty	Likes	Dislikes
    algorithms	Easy (47.94%)	1815	-
    给定一个整数数组 nums ，找到一个具有最大和的连续子数组（子数组最少包含一个元素），返回其最大和。

    示例:
    输入: [-2,1,-3,4,-1,2,1,-5,4],
    输出: 6
    解释: 连续子数组 [4,-1,2,1] 的和最大，为 6。
    进阶:

'''

# @lc code=start
from typing import List
import math

'''
    解法1 分治法求解： 
        Find_Max_Crossing_Subarray() ——O(n)
        Find_Max_Subarray() ——T(n)
            递归复杂度：
            T(n) = 2T(n/2)+ O(n)
        时间复杂度：O(nlog(n))
'''
'''
class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        l,h, val = Find_Max_Subarray(nums,0, len(nums)-1)
        return val

initial = -65535 #子数组求和 初始化近似负无穷
def Find_Max_Crossing_Subarray(A, low, high, mid):
    left_sum = initial
    max_left = -1
    sum = 0
    i = mid
    while(i>=low):       #迭代求解跨中点的最大和子数组的左边界
        sum = sum + A[i]
        if( sum>left_sum ):
            left_sum = sum
            max_left = i
        i -= 1

    right_sum = initial 
    max_right = -1
    sum = 0
    j = mid +1
    while(j<=high):      #迭代求解跨中点的最大和子数组的右边界
        sum = sum + A[j]
        if( sum>right_sum):
            right_sum = sum
            max_right = j
        j += 1
    return (max_left, max_right, left_sum+right_sum)



def Find_Max_Subarray(A, low, high):
    if(low == high):
        return (low, high, A[low])
    else:   #递归求解
        mid = math.floor((high + low)/2)
        (left_low, left_high, left_sum) = Find_Max_Subarray(A, low, mid)
        (right_low, right_high, right_sum) = Find_Max_Subarray(A, mid+1, high)
        (cross_low, cross_high, cross_sum) = Find_Max_Crossing_Subarray(A, low, high, mid)
        maximum = max(left_sum,right_sum,cross_sum)
        if(left_sum == maximum):
            return(left_low, left_high, left_sum)
        elif(right_sum == maximum):
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)
# @lc code=end

'''
'''
Accepted
202/202 cases passed (168 ms)
Your runtime beats 5.87 % of python3 submissions
Your memory usage beats 5.39 % of python3 submissions (14.3 MB)
'''

'''
    解法2 ： 类似剪枝
'''
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if len(nums) <1:
            return 0
        sum_nums = nums[0]
        maximum = sum_nums
        for i in range(1,len(nums)):
            if sum_nums <0:
                sum_nums = nums[i]
            else:
                sum_nums += nums[i]
            maximum = max(maximum, sum_nums)
            #print(maximum,sum_nums)
        return maximum 
            
'''
Accepted
202/202 cases passed (68 ms)
Your runtime beats 50.77 % of python3 submissions
Your memory usage beats 5.39 % of python3 submissions (14.1 MB)
'''