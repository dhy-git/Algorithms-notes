'''
    8.3 基数排序(非原址排序) 卡片排序机算法原理
        LSD排序算法:
            给定n个k位整数(d进制)，RadixSort稳定排序耗时O(d*(n+k))
'''
import math
def RadixSort(A,d=10):
    k = int(math.ceil(math.log(max(A),d)))      #确定最高位数（容器使用次数）
    for i in range(1,k+1):
        temp = [[] for i in range(d)]
        for val in A:
            temp[math.floor(val%(d**i)/(d**(i-1)))].append(val)         #放入容器
        #print(temp)
        del(A[:])
        A= [x for each in temp for x in each]      #容器中取出排序
    return A
A = [311,998,124,630,208,199,233,86,4,907,36,62,1,1028]
A = RadixSort(A)
print(A)
