'''
第4章 分治策略
4.1 最大子数组问题：
股票交易”低价买入，高价卖出“问题：
    给出一段时间内股票涨跌数据，求解买入卖出盈利最大的时间和盈利额。

'''
import math 

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
        if(left_sum >= right_sum and right_sum >= cross_sum):
            return(left_low, left_high, left_sum)
        elif(right_sum >= left_sum and left_sum >= cross_sum):
            return(right_low, right_high, right_sum)
        else:
            return(cross_low, cross_high, cross_sum)
    
    

L = [100,113,110,85,105,102,86,63,91,101,94,106,101,79,94,90,97]
# 首先求解子数组：
A = [0]
for i in range(0,len(L)-1):
    A.append(L[i+1]-L[i])
print('子数组：',A)
(low, high, sum) = Find_Max_Subarray(A, 1, len(A)-1)
print(low,high,sum)