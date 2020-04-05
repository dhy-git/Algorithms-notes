
'''
练习： 定义一个整型数组，并将指定个数的元素翻转到数组的尾部。
例如：(ar[], d, n) 将长度为 n 的 数组 arr 的前面 d 个元素翻转到数组尾部。
'''

def arrayvol(arr,d,n):
    if d > n:
        print('error')
        return 
    for i in range(d):
        arr.append(arr.pop(0))
    print(arr)

arr = [1,2,3,4,5,6,7]
print(arr)
arrayvol(arr, 5, len(arr))
