'''
第八章 线性时间排序
    8.2 计数排序
        不同于比较排序算法的时间复杂度下界 O(nlgn)， 计数排序下界更优，依赖于线性有限数据的范围
'''

def Count_Sort(A,B,k):
    C= [0 for i in range(k)]
    for i in range(len(A)):
        C[A[i]] += 1
    print('count:',C)
    for j in range(1,k):
        C[j] += C[j-1]
    print('index result:',C)
    for i in range(len(A)):
        B[C[A[i]]-1] = A[i]
        C[A[i]] -= 1

A = [5,7,3,5,2,6,9,1,0,4,8,5,7,3,2,9,0]
B = [ 0 for i in range(len(A))]
print("before sort",B)
Count_Sort(A,B,10)
print(B)