'''
2.3 设计算法
归并排序：引入分治策略，使用递归思想进行算法设计
时间复杂度 O(n) = nlogn
'''

import math

def Merge(L,R):
    A = []
    print(L,R)
    while L and R:
        if L[0]>R[0]:
            A.append(R.pop(0))
        else:
            A.append(L.pop(0))
    while L:
        A.append(L.pop(0))
    while R:
        A.append(R.pop(0))
    return A

def Merge_Sort(L):
    if (len(L) <2):
        return L
    middle = math.floor(len(L)/2)           #math模块中的floor方法，取不超过目标数的最大整数
    left, right = L[0:middle], L[middle:]
    #print(left,right)
    return Merge(Merge_Sort(left),Merge_Sort(right))


a = [10,9,8,7,6,5,4,3,2,1,0]
print('Merge sort result:',Merge_Sort(a))