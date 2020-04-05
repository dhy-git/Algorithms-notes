'''  第13章 红黑树
    数据结构与二叉搜索树相同，节点增加了表示颜色的存储位置
    通过颜色约束任意一条从根到叶子的路经长度，保证不存在路经二倍关系，因此确保树结构的近似平衡
    红黑树的五大特征：
        1.节点要么是红色，要么是黑色（红黑树名字由来）。
        2.根节点是黑色的
        3.每个叶节点(nil或空节点)是黑色的。
        4.每个红色节点的两个子节点都是黑色的（相连的两个节点不能都是红色的）。
        5.从任一个节点到其每个叶子节点的所有路径都是包含相同数量的黑色节点。
    从五大特征直观上总结出来几个点：
        1 对每个红色节点，子节点只有两种情况：要么都没有，要么都是黑色的。（不然会违反特征四）
        2 对黑色节点，如果只有一个子节点，那么这个子节点，必定是红色节点。（不然会违反特征五）
        3 假设从根节点到叶子节点中，黑色节点的个数是h, 那么树的高度H范围 h<= H <= 2H（特征四五决定）。
        第3点决定了 红黑树的查找不会退化到线性查找。查找时间复杂度为O(lgn)。
'''


'''
RB_Node    红黑树节点数据结构：
    is_black_node()
    set_black_node()
    set_red_node()
    print() 打印当前树
'''
class RB_Node:
    def __init__(self, val, color="R"):
        self.value = val
        self.color = color
        self.left = None
        self.right = None
        self.parent = None
        self.size = None

    def is_black_node(self):
        return self.color == "B"

    def set_black_node(self):
        self.color = "B"
 
    def set_red_node(self):
        self.color = "R"


class RBTree:
    def __init__(self):
        self.root = self.nil
        self.nil = RB_Node(None, "B")       #定义哨兵节点（nil.value==None, nil.color=="B"），作为红黑树的统一叶节点和根节点的双亲节点。

    # x节点左旋操作
    def left_rotate(self, x): 
        print("left rotate", x.value)
        #把y右子子点的左子点节赋给右节点x
        y = x.right
        x.right = y.left
        if y.left != self.nil:
            y.left.parent = x
        # x节点替换为y
        y.parent = x.parentzl
        if(x.parent == self.nil):
            self.root = y
        elif(x == x.parent.left):
            x.parent.left = y
        else:
            x.parent.right = y
        # x作为y的左子节点
        y.left = x
        x.parent = y
        return

    # y节点右旋操作
    def right_rotate(self, y):
        print("right rotate", y.value)
        # 处理步骤1
        x = y.left
        y.left = x.right
        # 处理步骤2
        x.parent = y.parent
        if(y.parent == self.nil):
            self.root = x
        elif(y.parent.left == y):
            y.parent.left = x
        else:
            y.parent.right = x
        # 处理步骤3      
        y.parent = x
        x.right = y

    #红黑树插入算法
    def RB_insert(self,z):
        y = self.nil
        x = self.root
        if(x != self.nil):
            y = x
            if(z.value < y.value):
                x = x.left
            else:
                x = x.right
        z.parent = y
        if(y == self.nil):
            self.root = z
        else:
            if(z.value < y.value):
                z = y.left
            else:
                z = y.right
        z.left = self.nil
        z.right = self.nil
        z.color = "R"
        RB_insertFixup(z)
        return z.value , 'color=', z.color

    #红黑树插入后平衡上色
    def RB_insertFixup(self,z):
        while(z.parent.color == "R"):
            '''z和父节点都是红色，则需要进行调整，调整过程分为两种情况'''
            # 情况1： z的父节点为左子节点
            if(z.parent.parent.left == z.parent):
                y = z.parent.parent.right
                # case1.1 叔节点也是红色
                if(y.color == "R"):
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.p.p       #调整结束，目标指向原节点的祖父节点
                # case1.2 z是右子节点，以父节点为基准左旋
                elif(z == z.parent.right):
                    z = z.parent
                    self.left_rotate(z)
                # case1.3 z为左子节点，右旋平衡树的深度
                z.parent.color = "B"
                z.parent.parent.color = "R"
                self.right_rotate(z.parent.parent)
            # 情况2： z的父节点为右子节点
            elif(z.parent.parent.right == z.parent):
                y = z.parent.parent.left
                # case2.1
                if(y.color == "R"):
                    z.parent.color = "B"
                    y.color = "B"
                    z.parent.parent.color = "R"
                    z = z.parent.parent
                # case2.2
                elif(z == z.parent.left):
                    z = z.parent
                    self.right_rotate(z)
                # case2.3
                z.parent.color = "B"
                z.parent.parent.color = "R"
                self.left_rotate(z.parent.parent)
        self.root.color = "B"
        return

    # 红黑树删除操作时需要的节点替换方法：
    def RB_transplant(self, u, v):
        if(u.parent = self.nil):
            self.root = v
        elif u == u.parent.left:
            u.parent.left = v
        else:
            u.parent.right = v
        v.parent = u.parent

    def RB_delete(self,z):
        y = z
        y_original_color = y.color
        #如果z的左子节点为空,右子节点直接替换
        if(z.left = self.nil):
            x = z.right
            self.RB_transplant(z, z.right)
        # 找到z右子树的最小节点，
        else:
            y = TreeMinimum(z.right)   ### 待完善
            y_original_color = y.color
            x = y.right
            if y.parent == z:
                x.parent = y
            else:
                self.RB_transplant(y, y.right)
                y.right = z.right
                y.right.parent = y
            self.RB_transplant(z, y)
            y.left = z.left
            y.left.parent = y
            y.color = z.color
        if y_original_color == "B":
            self.RB_deleteFixup(x)
           


def RB_deleteFixup(self, x):
    while x != self.root and x.color == "B":
        if x == x.parent.left:
            w = x.parent.right
            if w.color == "R":
                w.color = "B"
                x.parent.color = "R"
                self.left_rotate(x.parent)
                w = x.parent.right
            if w.left.color == "B" and w.right.color == "B":
                w.color = "R"
                x = x.parent
            else:
                if w.right.color == "B":
                    w.left.color = "B"
                    w.color = "R"
                    self.right_rotate(w)
                    w = x.parent.right
                w.color = x.parent.color
                x.parent.color = "B"
                w.right.color = "B"
                self.left_rotate(x.parent)
                x = self.root
        else:
            w = x.parent.left
            if w.color == "R":
                w.color = "B"
                x.parent.color = "R"
                self.right_rotate(x.parent)
                w = x.parent.left
            if w.right.color == "B" and w.left.color == "B":
                w.color = "B"
                x = x.parent
            else:
                if w.left.color == "B":
                    w.right.color = "B"
                    w.color = "R"
                    self.left_rotate(w)
                    w = x.parent.left
                w.color = x.parent.color
                x.parent.color = "B"
                w.left.color = "B"
                self.right_rotate(x.parent)
                x = self.root
    x.color = "B"
    
    def RB_TreeMinimum(self,x):
    while x.left != self.nil:
        x = x.left
    return x

    #中序遍历
    def Midsort(self, x):
    if x != None:
        self.Midsort(x.left)
        if x.value != 0:
            print('key:', x.value,'x.parent',x.parent.value)
        self.Midsort(x.right)

nodes = [11,2,14,1,7,15,5,8,4]
T = RBTree()
for node in nodes:
    print('插入数据',T.RB_insert(T,RBTreeNode(node)))
print('中序遍历')
T.Midsort(T.root)
T.RB_delete(T.root)
print('中序遍历')
T.Midsort(T.root)
T.RB_delete(T,T.root)
print('中序遍历')
T.Midsort(T.root)
