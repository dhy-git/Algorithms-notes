'''
汉诺塔递归问题：
    Hanoid(num, res, tar):
        num: 汉诺塔高度
        res：初始位置
        mid：中间过渡位置
        tar：目标位置
'''
flag = 0
def Hanoid(num, res, mid, tar):
    if(num == 1):
        global flag 
        flag+=1
        print('round %d: move from %s to %s' %(flag, res, tar))
    else:
        num -= 1
        Hanoid(num, res, tar, mid)
        Hanoid(1, res, mid, tar)
        Hanoid(num, mid, res, tar)
    return

Hanoid(3, 'A', 'B', 'C')
