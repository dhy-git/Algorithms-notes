'''第三部分 数据结构——包括基本数据结构的构建和操作实现'''

'''
>>> 1. 栈 Stack  
    特性：先进后出的数据结构
    栈顶，栈尾
    Stack() 创建一个空的新栈。 它不需要参数，并返回一个空栈。
    push(item)将一个新项添加到栈的顶部。它需要 item 做参数并不返回任何内容。
    pop() 从栈中删除顶部项。它不需要参数并返回 item 。栈被修改。
    peek() 从栈返回顶部项，但不会删除它。不需要参数。 不修改栈。
    isEmpty() 测试栈是否为空。不需要参数，并返回布尔值。
    size() 返回栈中的 item 数量。不需要参数，并返回一个整数。
'''
class Stack():
    def __init__(self):
        self.items = []
    def push(self,item):
        self.items.append(item)
    def pop(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop()
    def isEmpty(self):
        return self.items == []
    def peek(self):
        return self.items[len(self.items)-1]
    def size(self):
        return len(self.items)    

print('栈操作范例')
s = Stack()
print(s.size())
s.push(69)
print(s.pop())

'''
>>> 2. 队列 Queue
    特性：先进先出
    Queue() 创建一个空的新队列。 它不需要参数，并返回一个空队列。
    enqueue(item) 将新项添加到队尾。 它需要 item 作为参数，并不返回任何内容。
    dequeue() 从队首移除项。它不需要参数并返回 item。 队列被修改。
    isEmpty() 查看队列是否为空。它不需要参数，并返回布尔值。
    size() 返回队列中的项数。它不需要参数，并返回一个整数。
    travel() 遍历当前队列缓存
'''
class Queue():
    def __init__(self):
        self.items = []
    def enqueue(self,item):
        self.items.insert(0,item)
    def dequeue(self):
        if self.isEmpty():
            return None
        else:
            return self.items.pop() 
    def isEmpty(self):
        if self.items == []:
            print("queue is empty") 
            return True
        else:
            return False
    def size(self):
        return len(self.items)
    def travel(self):
        print(self.items)

print('#队列操作')
q = Queue()
q.isEmpty()
q.enqueue('this')
q.travel()
q.dequeue()
q.dequeue()

'''
>>> 3. 链表
        Step 1: Node_L
            __init_(): initialize the node with the data
            self.data: the value stored in the node
            self.next: the reference pointer to the next node
            check(): compare a value with the node value
        Step 2: Single-Linked List
            __init__(): 初始化方法
            length():返回节点数
            output(): 打印方法
            add(): 添加一个节点到list 中
            search(): 在列表中查找具有指定值的节点
            remove(): 通过节点id 移除节点
        Step 3: 扩展node结构，生成双链表节点Node_D
            __init_(): initialize the node with the data
            self.data: the value stored in the node
            self.next: the reference pointer to the next node
            self.previous:
            check(): compare a value with the node value
        Step 4: DoubleLinkedList
            __init__
            DL_length
            DL_output
            DL_search
'''
#step 1
class Node_L:
    def __init__(self, data):
        self.data = data
        self.next = None
        return
    def check(self, value):
        if self.data == value:
            return True
        else:
            return False

#step 2
class SingleLinkedList:  
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def add(self, item):
        if not isinstance(item, Node_L):  #如果不是 Node，构建为Node
            item = Node_L(item)
        if self.head is None:           #如果头节点是空，则当前节点就是 item
            self.head = item
        else:
            self.tail.next = item       #如果已经有头节点，则加到尾部
        self.tail = item         #尾部就是当前item
        return

    def length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            count = count + 1
            current_node = current_node.next
        return count

    def output(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            current_node = current_node.next
        return

    #search the linked list for the node that has this value
    def search(self, value):
        current_node = self.head
        node_id = 1         # define position
        results = []        # define list of results
        while current_node is not None:
            if current_node.check(value):
                results.append(node_id)
            current_node = current_node.next
            node_id = node_id + 1
        return results

    def remove(self, item_id):
        current_id = 1
        current_node = self.head
        previous_node = None
        while current_node is not None:
            #当前这个node 就是需要移除的node
            if current_id == item_id:
                # if this is the first node (head)
                #如果这个node 前面还有node ，那需要把前面node 的next，指向当前node 的下一个node（原来前一个node 的next 是当前node）。
                # 就已经从这个链路里移除了，因为没有node 指向它了。
                if previous_node is not None:
                    previous_node.next = current_node.next
                else:
                    #需要移除的是第一个node，只要把当前的head 指向下一个node 即可
                    self.head = current_node.next
                    return
            # needed for the next iteration
            # 如果还不是当前node，上一个node 变成当前node
            # 当前node 变成当前node 的下一个。当然id 要加1
            previous_node = current_node
            current_node = current_node.next
            current_id = current_id + 1
        return


'''
单链表数据结构测试代码
    print('**************单链表测试代码***************')
    l = SingleLinkedList()
    l.add("Jack")
    l.output()
    A = l.search("Jack")
    print(A)
    l.add("Danny")
    l.add("Sirius")
    l.add("Potter")
    l.remove(2)
    l.output()
    print('LinkedList length',l.length())
'''
#Step 3: Creating a Double-Linked Node
class Node_D:        #可以考虑继承单链表数据结构Node，复用Node方法
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
        return
    def check(self, value):
        if self.data == value:
            return True
        else:
            return False

#Step 4: Creating a Double-Linked List
class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        return

    def DL_add(self, item):
        "add an item at the end of the list"
        if not isinstance(item, Node_D):
            item = Node_D(item)
        else: 
            #如果还没有Node，则首尾都是item，而且该node 的前一个没有，后一个也没有
            if self.head is None:
                self.head = item
                #item.previous = None
                #item.next = None
                self.tail = item
            else:
                #如果有Node 元素了，则当前尾部的node的下一个node 就是item，item的前一个元素就是当前的tail node。现在把item 放到尾部。
                self.tail.next = item
                item.previous = self.tail
                self.tail = item
        return

    #根据node id 移除node
    def DL_remove(self, item_id):
        "remove the list item with the item id"
        current_id = 1
        current_node = self.head
        #当前node 不为空
        while current_node is not None:
            previous_node = current_node.previous
            next_node = current_node.next
            #当前node 就是需要移除的node
            if current_id == item_id:
                # if this is the first node (head)
                #当前node 不是第一个head node
                if previous_node is not None:
                    #前一个node的 next 指向 下个node
                    previous_node.next = next_node
                    # 如果当前node 不是tail node
                    
                    if next_node is not None:
                        # next_node 前一个node 指向 当前node 的前一个node（原来next_node 的前一个node 是 当前node）
                        next_node.previous = previous_node
                else:
                    #如果需要移除的是head node，则把head 指向 next_node
                    self.head = next_node
                    # 如果 head node 不是最后一个node ，则还要把下一个node 的 previous 指向为None（原来为当前node）
                    if next_node is not None:
                        next_node.previous = None
                # we don't have to look any further
                return
            # needed for the next iteration
            current_node = next_node
            current_id = current_id + 1
        return

    def DL_length(self):
        count = 0
        current_node = self.head
        while current_node is not None:
            # increase counter by one
            count = count + 1
            # jump to the linked node
            current_node = current_node.next
        return count

    def DL_output(self):
        "outputs the list (the value of the node, actually)"
        current_node = self.head
        while current_node is not None:
            print(current_node.data)
            # jump to the linked node
            current_node = current_node.next
        return

    def DL_search (self, value):
        "search the linked list for the node that has this value"
        # define current_node
        current_node = self.head
        # define position
        node_id = 1
        # define list of results
        results = []
        while current_node is not None:
            if current_node.check(value):
                results.append(node_id)
            # jump to the linked node
            current_node = current_node.next
            node_id = node_id + 1
        return results

    

