'''
第6章 堆排序
    建立二叉数据结构，进行堆处理 时间复杂度O(nlgn)
        算法实现包括：
        最大堆（最小堆）的维护处理函数
        建立最大堆(最小堆)函数
        堆排序函数
'''
import math 

A = [4,1,3,2,16,9,10,14,8,7]


Parent = lambda i: i/2
Left = lambda i: 2*i
Right = lambda i: 2*i+1


'''
Msx_Heapify 维护最大堆性质的重要过程
    输入：数组A 和下标i
'''
def Max_Heapify(A, i):
    l = Left(i)
    r = Right(i)
    if(l<=HeapSize and A[l]>A[i]):
        largest = l
    else:
        largest = i
    if(r <= HeapSize and A[r]>A[i]):
        largest = r
    if(largest != i):
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(A, largest)


def Build_Max_heap(A):
    max = math.floor(len(A)/2)
    for i in range(max, 1, -1):
        Max_Heapify(A, i)

def HeapSort(A):

    Build_Max_heap(A)
    for i in range(len(A),2,-1):
        A[i], A[1] = A[1], A[i]
        ##HeapSize -= 1
        Max_Heapify(A, 1)


A.insert(0,0)   #下标对齐
HeapSize = len(A)   #定义堆的大小
HeapSort(A)
print(A)

#def Max_Heap_Insert():

#def Heap_Extract_Max():  

#def Heap_Increase_Key():

#def Heap_Maximum():

