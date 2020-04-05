'''
第2章 算法基础
2.1 插入排序——引入算法设计：循环不变式
    循环不变式的三条性质：
        初始化：循环的第一次迭代前为真
        保持： 保证下一次迭代为真
        终止： 循环结束证明算法正确
    时间复杂度O(n^2)
'''

def Insertion_Sort(array):
    max = len(array)
    for i in range(1,max):
        temp = array[i]
        # insert:
        j = i-1
        while(j>=0 and array[j]>temp):
            array[j+1] = array[j]
            j = j - 1
        array[j+1] = temp
        print(array)

a = [0,12,2,2,2,43,4,1]
Insertion_Sort(a)


