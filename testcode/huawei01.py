#coding=utf-8

'''
给出二叉树节点数和每个节点的深度，计算可能的种类
'''
import sys

#阶乘
def fun(n):
    if n ==0:
        return 1
    else:
        return n*(fun(n-1))



if __name__ == "__main__":
    # 读取第一行的n
    n = int(sys.stdin.readline().strip())
    line = sys.stdin.readline().strip()
    values = list(map(int, line.split()))
    #print(n,values)
    max_deep = max(values)
    if max_deep == 0:
        print(1)
    #哈希表统计特定深度节点个数
    map_node = dict()
    for each in values:
        if each not in map_node:
            map_node[each] = 1 
        else:
            map_node[each] +=1
            
    #计算二叉树种类总数
    count = 1
    for i in range(1, max_deep+1):
        #i层节点分布种类
        P=1
        if map_node[i]< 2*map_node[i-1]:        #i层未满
            #组合
            P = int( fun(2*map_node[i-1]) / ( fun(map_node[i]) * fun(2*map_node[i-1] - map_node[i]) ))
        #累计可能性
        count *= P
    print(count)
        

