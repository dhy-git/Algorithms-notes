'''
第五部分 高级数据结构
    第1章 B树、2-3树
        B树是一种平衡多叉树，用于磁盘、数据库信息管理
        阶为M的B树具有下列结构特征：
            1.树的根或者是一片树叶，或者其儿子数在2和M之间。
            2.除根节点外的所有非树叶节点儿子数在┌M/2┐和 M之间。
            3.所有的树叶都在相同的高度。    
            4.节点中包括n个关键字，n+1个指针，一般形式为：
                    （n,P0,K1,P1,K2,P2,…,Kn,Pn）。
                每个结点中关键字从小到大排列，
                当该结点的孩子是非叶子结点时，该k-1个关键字正好是k个儿子包含的关键字的值域的分划。

        二叉树插入操作：（以特殊情况M=3为例， 此时B树为2-3树）
            1. 未满节点插入关键字
            2. 已满节点插入关键字
                需要对该节点进行分裂（按照插入关键字和已有关键字大小关系分为三种情况）
                    A. 父节点未满： 插入父节点
                    B. 父节点已满： 分裂父节点，向上递归


'''

'''
    2-3树节点定义
'''
class Node(object):
    def __init__(self,key):
        self.key1 = key
        self.key2 = None
        self.left = None
        self.middle = None
        self.right = None
    def isLeaf(self):
        return self.left is None and self.middle is None and self.right is None
    def isFull(self):
        return self.key2 is not None
    def hasKey(self,key):
        if (self.key1==key) or (self.key2 is not None and self.key2==key):
            return True
        else:
            return False
    def getChild(self,key):
        if key<self.key1:
            return self.left
        elif self.key2 is None:
            return self.middle
        elif key<self.key2:
            return self.middle
        else:
            return self.right

class Tree_2_3(object):
    def __init__(self):
        self.root = None

    #get 方法查找关键字，返回查找结果     
    def get(self,key):
        if self.root is None:
            return None
        else:
            return self._get(self.root,key)
    def _get(self,node,key):
        if node is None:
            return None
        elif node.hasKey(key):
            return node
        else:
            child=node.getChild(key)
            return self._get(child,key)

     #插入节点     
    def put(self,key):
        if self.root is None:
            self.root=Node(key)
        else:
            pKey,pRef = self._put(self.root,key)
            if pKey is not None:
                newnode = Node(pKey)
                newnode.left=self.root
                newnode.middle=pRef
                self.root=newnode
    def _put(self,node,key):
        if node.hasKey(key):
            return None,None
        elif node.isLeaf():
            return self._addtoNode(node,key,None)
        else:
            child=node.getChild(key)
            pKey,pRef=self._put(child,key)
            if pKey is None:
                return None,None
            else:
                return self._addtoNode(node,pKey,pRef)
             
         
    def _addtoNode(self,node,key,pRef):
        if node.isFull():
            return self._splitNode(node,key,pRef)
        else:
            if key<node.key1:
                node.key2=node.key1
                node.key1=key
                if pRef is not None:
                    node.right=node.middle
                    node.middle=pRef
            else:
                node.key2=key
                if pRef is not None:
                    node.right=pRef
            return None,None
    def _splitNode(self,node,key,pRef):
        newnode=Node(None)
        if key<node.key1:
            pKey=node.key1
            node.key1=key
            newnode.key1=node.key2
            if pRef is not None:
                newnode.left=node.middle
                newnode.middle=node.right
                node.middle=pRef
        elif key<node.key2:
            pKey=key
            newnode.key1=node.key2
            if pRef is not None:
                newnode.left=pRef
                newnode.middle=node.right
        else:
            pKey=node.key2
            newnode.key1=key
            if pRef is not None:
                newnode.left=node.right
                newnode.middle=pRef
        node.key2=None
        return pKey,newnode