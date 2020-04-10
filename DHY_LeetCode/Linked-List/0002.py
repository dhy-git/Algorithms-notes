'''
>>>两数相加
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (35.98%)	4156	-

    给出两个 非空 的链表用来表示两个非负的整数。
    其中，它们各自的位数是按照 逆序 的方式存储的，并且它们的每个节点只能存储 一位 数字。
    如果，我们将这两个数相加起来，则会返回一个新的链表来表示它们的和。
    您可以假设除了数字 0 之外，这两个数都不会以 0 开头。

    示例：
    输入：(2 -> 4 -> 3) + (5 -> 6 -> 4)
    输出：7 -> 0 -> 8
    原因：342 + 465 = 807
'''

'''
    解法1 ： 还原数值计算后重建链表
'''
# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        num1 = self.translink_to_10(l1)
        num2 = self.translink_to_10(l2)
        num = num1+ num2
        if num == 0:
            return ListNode(0)

        head = ListNode(None)
        cr = head
        while(num > 0):
            k = num%10
            node = ListNode(k)
            cr.next = node
            cr = node
            num = num//10       
        #print(head.next.val)
        return head.next

    def translink_to_10(self, L:ListNode) -> int:
        num = 0
        temp = L
        i = 0
        while temp != None:
            num += temp.val*(10**i)
            i += 1
            temp = temp.next
        return num
'''
# @lc code=end

'''
    解法2 ：链表操作 按位计算
'''
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        cr = head #链表指针
        s = 0 #进位标志
        while(l1 or l2):
            num1 = l1.val if l1 else 0
            num2 = l2.val if l2 else 0
            n = (num1+num2+s)%10
            cr.next = ListNode(n)
            s = (num1+num2+s)//10
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            cr = cr.next
        if s == 1:
            cr.next = ListNode(1)
        return head.next