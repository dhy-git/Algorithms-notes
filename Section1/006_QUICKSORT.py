'''
第7章 快速排序
    与归并排序类似，使用分治策略：
    关键环节： 合理分割数组进行递归排序

'''
def Partition(A,p,r):
    i = p-1
    for j in range(p,r):
        if(A[j] <= A[r]):
            i += 1
            A[i],A[j] = A[j],A[i]
    A[i+1],A[r] = A[r],A[i+1]
    return i+1

def QuickSort(A,p,r):
    if(p<r):
        index = Partition(A,p,r)
        QuickSort(A,p,index-1)
        QuickSort(A,index+1,r)

A = [5,7,3,5,2,6,9,1,0,4,8,5,7,3,2,9,0]
QuickSort(A,0,len(A)-1)
print(len(A),A)


'''
快速排序的随机化版本：使用随机函数选定主元
    适用于大数据输入下的排序，改善期望值，提高平均情况性能
'''
from random import randrange
def Random_Partition(A,p,r):
    i = randrange(p,r)
    A[i],A[r] = A[r],A[i]
    return Partition(A,p,r)

def Random_QuickSort(A,p,r):
    if(p<r):
        index = Random_Partition(A,p,r)
        Random_QuickSort(A,p,index-1)
        Random_QuickSort(A,index+1,r)
A = [5,7,3,5,2,6,9,1,0,4,8,5,7,3,2,9,0]
Random_QuickSort(A,0,len(A)-1)
print(len(A),A)
