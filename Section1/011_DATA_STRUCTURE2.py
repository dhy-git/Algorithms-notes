''' >>> 4. 二叉树：
    step 1: 创建二叉树节点数据结构 BT_Node
        self.value 存储节点数据
        self.left  指向左子树
        self.right 指向右子树
        self.p 指向双亲节点
    step 2: 创建二叉树BinaryTree()
        基本存储结果（根节点，初始化列表等）：
            self.root
            self.creat_list     #非必要参数
            self.tree           #非必要参数
        定义二叉树的建立方法：
            creat_bylist  先序序列创建二叉树
            create_bypm 前序、中序解析创建二叉树： 
                前序序列确定根节点，
                索引中序划分左右子树，
                迭代实现二叉树构建

'''

class BT_Node():
    def __init__(self, value):
        self.value = value
        self.left = None       #左子树
        self.right = None      #右子树
        self.p = None
    

class BinaryTree():
    def __init__(self):
        self.root = None
        self.create_list = []    #输入的先序序列，用于创建二叉树
        self.tree = []          #存放正在操作的节点
        pass

    #通过先序序列创建二叉树，没有左右子节点被标记为'#'
    def create_bylist(self):
        current = self.create_list.pop(0)
        if current != '#':
            new_node = BT_Node(current)
            if self.root is None:
                self.root = new_node
            new_node.left = self.create_bylist()
            if(new_node.left != None):
                new_node.left.p = new_node
            new_node.right = self.create_bylist()
            if(new_node.right != None):
                new_node.right.p = new_node
            return new_node
        return None

        
    #通过前序序列和中序序列创建二叉树
    def create_bypm(self, pre_order, mid_order):
        if len(pre_order) == 0:
            return None
        new_node = BT_Node(pre_order[0])
        if self.root is None:
            self.root = new_node
        i = mid_order.index(pre_order[0])
        #print(i)
        new_node.left = self.create_bypm(pre_order[1:1+i], mid_order[:i])
        if(new_node.left != None):
            new_node.left.p = new_node
        new_node.right = self.create_bypm(pre_order[1+i:], mid_order[i+1:])
        if(new_node.right != None):
            new_node.right.p = new_node
        return new_node

    #通过中序和后序创建二叉树
    def create_bymp(self, mid_order, post_order):
        length = len(post_order)
        if length == 0:
            return None
        new_node = BT_Node(post_order[-1])
        if self.root is None:
            self.root = new_node
        i = mid_order.index(post_order[-1])
        new_node.left = self.create_bymp(mid_order[:i], post_order[:i])
        if(new_node.left != None):
            new_node.left.p = new_node
        new_node.right = self.create_bymp(mid_order[i+1:], post_order[length-2-i:length-1])
        if(new_node.right != None):
            new_node.right.p = new_node
        return new_node

    #通过递归进行先序遍历
    def recursion_vlr(self, root):
        if root is None:
            return
        print(root.value)
        self.recursion_vlr(root.left)
        self.recursion_vlr(root.right)

    #通过栈非递归进行先序遍历
    def pre_order_stack(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                print(node.value)
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            node = node.right

    #通过递归进行中序遍历
    def recursion_lvr(self, root):
        if root is None:
            return
        self.recursion_lvr(root.left)
        print(root.value)
        self.recursion_lvr(root.right)

    #通过栈非递归进行中序遍历
    def mid_order_stack(self, root):
        if root is None:
            return
        mystack = []
        node = root
        while mystack or node:
            while node:
                mystack.append(node)
                node = node.left
            node = mystack.pop()
            print(node.value)
            node = node.right

    #通过递归进行后序遍历
    def recursion_lrv(self, root):
        if root is None:
            return
        self.recursion_lrv(root.left)
        self.recursion_lrv(root.right)
        print(root.value)

    #通过栈非递归进行后序遍历，先遍历右子树，在遍历左子树，最后逆序数出
    def post_order_stack(self, root):
        if root is None:
            return
        mystack1 = []
        #stack2是为了逆序输出，全都存在2栈中，1栈的作用是按照右、左的顺序遍历节点存入2栈
        mystack2 = []
        node = root
        while mystack1 or node:
            while node:
                mystack2.append(node)
                mystack1.append(node)
                node = node.right
            node = mystack1.pop()
            node = node.left
        while mystack2:
            print(mystack2.pop().value)

    #利用队列进行广度优先遍历BFS
    def level_scan(self):
        queue = []
        current = self.root
        queue.append(current)
        while queue:
            current = queue.pop(0)
            print(current.value)
            if current.left:
                queue.append(current.left)
            if current.right:
                queue.append(current.right)
    

    #二叉树层数计算
    def layer_count(self,root):
        if(root == None):
            return 0
        else:
            l = self.layer_count(root.left) + 1
            r = self.layer_count(root.right) + 1
        return max(l, r)
    
    #二叉树查找节点, 未查找到返回None
    def search(self, value):
        node = self.root
        while(node != None):
            if(value < node.value):
                node = node.left
            elif(value > node.value):
                node = node.right
            else:
                return node
        return None


    #二叉搜索树插入节点
    def insert(self, value):
        new = BT_Node(value)
        temp = BT_Node(None)
        node = self.root
        while(node != None):
            temp = node
            if(new.value == node.value):     #二叉树节点唯一时，存在则停止插入
                print("node is alread exist")
            elif(new.value < node.value):
                node = node.left
            else:
                node = node.right
        if(temp == None):
            self.root = new
        elif(new.value < temp.value):
            temp.left = new
        else:
            temp.right = new
   
    #镜像二叉树操作（Google面试递归经典问题）
    def invert(self, node):
        if(node == None):
            return None
        else:
            left = self.invert(node.left)
            right = self.invert(node.right)

            node.left = right
            node.right = left
        return node


    #二叉树节点替换方法：节点u为被替换节点， v为替换后节点
    def transplant(self,u,v):
        if(self.root == u):
            self.root = v
        elif(u == u.p.left):
            u.p.left = v
        else:
            u.p.right = v
        if(v.value != None):
            v.p = u.p


    '''
    节点删除存在的问题：
        由于数据结构定义关系，二叉搜索树叶节点左右子树为空：
        （node.left不是BT_Node类），无法使用transplant方法进行节点替换
        因此在处理叶节点相关的问题时需要额外判断，如何简化判断问题待定
    '''
    def delete(self, value):
        ret = self.search(value)        #找到待删除的目标节点
        if(ret == None):
            print("target is not exist")
            return
        else:
            print("target located",ret.value)
        #情况1 左子树空，
        if(ret.left == None):
            self.transplant(ret, ret.right)
        #情况2 右子树空
        elif(ret.right == None):
            self.transplant(ret,ret.left)
        #情况3 左右子树非空
        else:
            #找到目标节点的后继节点mini_node
            mini_node = ret.right
            while(mini_node.left != None):
                mini_node = mini_node.left
            if(mini_node.p != ret):
                self.transplant(mini_node,mini_node.right)
                mini_node.right = ret.right
                mini_node.right.p = mini_node 
            self.transplant(ret,mini_node)
            mini_node.left = ret.left
            mini_node.left.p = mini_node
        

'''  test code for Biniary Tree:

    pre_str = 'ABDGHCEIF'
    mid_str = 'GDHBAEICF'
    las_str = 'GHDBIEFCA'
    p_list = [each for each in pre_str]
    m_list = [each for each in mid_str]
    l_list = [each for each in las_str]

    mytree = BinaryTree()
    mytree.create_tree(p_list,m_list)
    print('遍历二叉树')
    mytree.recursion_lrv(mytree.root)   #后序
'''

#二叉搜索树测试代码
pre = [14,6,3,2,1,5,4,10,8,7,9,12,11,13,16,15,18,17,19]
mid = [i for i in range(1,20)]

pre1 = [12,5,2,9,18,15,17,19]
mid1 = [2,5,9,12,15,17,18,19]
ST = BinaryTree()
ST.create_bypm(pre1, mid1)
print('insert num')
ST.insert(16)
print('中序遍历搜索二叉树') 
ST.recursion_lvr(ST.root)
num = ST.layer_count(ST.root)
print("this binaray tree's layer is ",num)
ret = ST.search(115)
if(ret == None):
    print("未查找到，目标不存在")
else:
    print('目标查询完成',ret.value)

ST.delete(15)
print('中序遍历搜索二叉树') 
ST.recursion_lvr(ST.root)
num = ST.layer_count(ST.root)
print("this binaray tree's layer is ",num)

ST.invert(ST.root)
print('中序遍历搜索二叉树') 
ST.recursion_lvr(ST.root)