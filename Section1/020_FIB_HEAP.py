'''
第20章 斐波那契堆
    是一系列具有最小堆序的有根树的集合，任意节点的所有孩子连接为双向链表（x的孩子链表）
    包含可合并堆操作
    在常数摊还时间内完成计算
'''
import math

#斐波那契堆数据结构：
class FIB_HEAP_NODE:
    def __init__(self, key):
        self.key = key #关键字
        self.degree = 0 #元素在堆中的度
        self.p = 0 #指向双亲节点
        self.child = 0 #指向第一个孩子节点
        self.left = 0 #左向循环指针
        self.right = 0 #右向循环指针
        self.mark = False #标记节点的操作历史， 得到需要的时间界

    #添加cn到FIB_HEAP的子节点中
    def GetChild(self,cn):
        cn.p = self
        self.degree = self.degree+1
        if self.child == 0:
            self.child = cn
            cn.left = cn
            cn.right = cn
        else:
            c = self.child
            cn.right = c
            cn.left = c.left
            cn.left.right = cn

    #打印当前节点的所有同级节点以及各自的子节点
    def printNode(self):
        if self.child != 0:
            c = self.child
            cl = c.left
            while True:
                print("%d has child: %d" % (self.key,c.key))
                c.printNode()
                if cl == c:
                    break
                c = c.right

    #查询节点
    def SearchChild(self, key):
        w = self
        end = self
        resultnode = 0
        while True:
            if w.key == key:
                return w
            if w.child != 0:
                resultnode = w.child.SearchChild(key)
            if resultnode != 0:
                return resultnode
            w = w.right
            if w == end:
                return 0

#创建斐波那契堆（对象初始化）
def MakeHeap():
    return FIBHEAP(0,0)


class FIBHEAP:
    def __init__(self, n, minx):
        self.n=n #堆大小
        self.min=minx #最小节点的指针

    def Insert(self, x):    #put on the left of min
        if self.min==0:
            self.min=x
            x.left=x
            x.right=x
        else:
            x.right=self.min
            x.left=self.min.left
            x.left.right=x
            self.min.left=x
            if x.key < self.min.key:
                self.min=x
        self.n=self.n+1

    def Minimum(self):
        return self.min
    
    #从堆 H 中删除最小关键字的元素，并返回一个指向该元素的指针
    def ExtractMin(self):
        z = self.min
        if z != 0:
            if z.child != 0:
                c = z.child
                #待删除节点的所有子节点插入堆的根链表中
                while c.p != 0:
                    cpr=c.left
                    c.p = 0
                    c.left = 0
                    c.right = 0
                    c.right = self.min
                    c.left = self.min.left
                    c.left.right = c
                    self.min.left = c
                    c = cpr
            #删除最小节点z
            z.right.left = z.left
            z.left.right = z.right
            z.child = 0
            if z == z.right:
                self.min = 0
            else:
                self.min = z.right
                self.Consolidate()
            self.n = self.n-1
        return z

    #减少堆中树的数目，保证同一个度的树只有一个
    def Consolidate(self):
        #分配数组A大小 = 可合并堆的最大度数上界 
        A = []
        for i in range(0, int(math.log(self.n,2) + 1)):
            A.append(0)
        w = self.min
        t = w.left
        while True:
            x = w
            print('is %d' % w.key)
            d = x.degree
            #链表遍历同级节点，初始化A数组，查找循环链表，A[d]存储d度下最小节点x
            while A[d] != 0:
                y = A[d]
                if x.key > y.key:
                    v = x
                    x = y
                    y = v
                self.Link(y,x)      # 交换后y.key较大，调整为x的子节点
                A[d] = 0
                d = d + 1           #重新连接后节点度+1
            A[d] = x
            if w == t:
                break
            w = x.right
        #最小堆集合合并完成，链接H.min到最小节点：
        self.min = 0
        for i in range(0,int(math.log(self.n,2) + 1)):
            if A[i] != 0:
                if self.min == 0:
                    self.min = A[i]
                    A[i].left = A[i]
                    A[i].right = A[i]
                else:
                    A[i].right = self.min
                    A[i].left = self.min.left
                    A[i].left.right = A[i]
                    self.min.left = A[i]
                    if A[i].key < self.min.key:
                        self.min = A[i] 

    #将节点 y链接作为x的子节点
    def Link(self,y,x):
        y.right.left = y.left
        y.left.right = y.right
        y.p = x
        x.degree = x.degree+1
        y.mark = False
        if x.child == 0:
            x.child = y
            y.left = y
            y.right = y
        else:
            c = x.child
            y.right = c
            y.left = c.left
            y.left.right = y 
            c.left = y

    # 将堆H中元素x的关键字变为k（降值操作），并相应的改变元素x在堆中的位置
    def DecreaseKey(self,x,k):
        #根据替换关键字找到堆中的节点X
        x = self.min.SearchChild(x)
        if k > x.key:
            print("error: new key is greater than current key")
        x.key = k
        y = x.p
        #降值后判断与父节点大小关系：
        if y != 0 and x.key < y.key:
            self.Cut(x,y)
            self.CasCut(y)
        if x.key < self.min.key:
            self.min = x

    #切断 x 和其父节点 y 之间的链接，使 x 成为根节点
    def Cut(self,x,y):
        # 1. 断开x 与 y、同级子节点的链接
        if y.degree == 1:           #父节点仅有x一个子节点
            y.child = 0
            x.p = 0
        else:
            w = x.right
            if x == y.child:
                y.child = w
            w.left = x.left
            x.left.right = x.right
            
        # 2. 在H.min和其左侧节点之间插入x及其子树
        y.degree = y.degree-1
        x.right = self.min
        x.left = self.min.left
        x.left.right = x
        self.min.left = x
        # 3. 若x.key为最小值：
        if x.key < self.min.key:
            self.min = x
        x.p = 0
        x.mark = False

    def CasCut(self,y):
        z = y.p
        if z != 0:
            if y.mark == False:
                y.mark = True
            else:
                self.Cut(y,z)
                self.CasCut(z)


#合并堆
def Union(H1, H2):
    H = MakeHeap()
    #第一步 链接最小堆节点H.min
    if H1.min==0 or H1.min.key > H2.min.key:
        H.min = H2.min
    else:
        H.min = H1.min
    H.n = H1.n + H2.n
    #堆不为空时 补全H1 H2构成的双向链表
    if H1.min != 0 and H2.min != 0:
        xr = H1.min.right

        H1.min.right = H2.min
        H2.min.left.right = xr

        xr.left = H2.min.left
        H2.min.left = H1.min
    return H 




