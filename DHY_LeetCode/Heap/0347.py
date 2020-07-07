'''
    最大堆解法：
        1，构造哈希表计频
        2、哈希表key建立最大堆，最大堆比较依据哈希表键值
        3、堆排序
        4、输出取前k个高频元素
    注：可优化:
        构建HeapSize = k 的最大堆，其余元素比较进堆
        

'''
# [347] 前 K 个高频元素
#

# @lc code=start
from typing import List
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        num_map = dict()
        for each in nums:
            if each not in num_map:
                num_map[each] = 1
            else:
                num_map[each] +=1
        #print(num_map)
        A = Heap_Sort(num_map)
        return A[len(A)-k:]

def Max_Heapify(Map: dict, A: List[int], HeapSize, i):
    Left = i*2
    Right = i*2+1
    if (Left <HeapSize and Map[A[Left]]>= Map[A[i]]):
        largest = Left
    else:
        largest = i
    if (Right <HeapSize and Map[A[Right]]>= Map[A[largest]]):
        largest = Right
    if (largest != i):
        A[i], A[largest] = A[largest], A[i]
        Max_Heapify(Map, A, HeapSize, largest)

def Build_Max_Heap(Map: dict, A: List[int], HeapSize):
    maximum = int(HeapSize/2)
    for i in range(maximum,-1, -1):
        Max_Heapify(Map, A, HeapSize, i)

def Heap_Sort(Map : dict):
    A = list(Map.keys())
    HeapSize = len(A)
    Build_Max_Heap(Map, A, HeapSize)
    for i in range(len(A)-1, 0, -1):
        A[i], A[0] = A[0], A[i]
        HeapSize -=1
        Max_Heapify(Map, A, HeapSize, 0)
    return A

'''
Accepted
21/21 cases passed (80 ms)
Your runtime beats 33.17 % of python3 submissions
Your memory usage beats 100 % of python3 submissions (16.6 MB)
'''


# @lc code=end

