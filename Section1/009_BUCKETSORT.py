'''
    8.4 桶排序 
        假设输入服从均匀分布[0,1), 平均情况时间代价O(n)：
            条件：所有桶的大小的平方和与总的元素数呈线性关系，桶排序就可以在线性时间内完成
'''
#桶B[i]内元素的插入排序子函数
def sort(A):
    for i in range(1,len(A)):
        temp = A[i]
        j = i-1
        while(j>=0 and temp<A[j]):
            A[j+1] = A[j]
            j -= 1
        A[j+1] = temp

def BucketSort(A):
    min_num = min(A)
    max_num = max(A)
    bucket_size = (max_num - min_num)/(len(A)-1)
    temp = [[] for i in range(len(A))]
    for each in A:
        temp[int(each//bucket_size)].append(each)
    for i in temp:
        sort(i)
    del(A[:])
    A = [x for each in temp for x in each]
    print(A)

a = [0.83, 0.13, 0.73, 0.29, 0.30, 0.5, 0.42]
BucketSort(a)
print(a)