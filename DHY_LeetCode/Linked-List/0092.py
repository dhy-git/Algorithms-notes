'''
>>>反转链表 II
    Category	Difficulty	Likes	Dislikes
    algorithms	Medium (47.83%)	339	-
    反转从位置 m 到 n 的链表。请使用一趟扫描完成反转。

    说明:
    1 ≤ m ≤ n ≤ 链表长度。

    示例:
    输入: 1->2->3->4->5->NULL, m = 2, n = 4
    输出: 1->4->3->2->5->NULL
'''

# @lc code=start
#Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def reverseBetween(self, head: ListNode, m: int, n: int) -> ListNode:
        h = ListNode(None)
        locate = h

        cr = head
        count = 1
        #前m-1 不翻转
        while(count < m):
            #按序建立前m-1个
            node = ListNode(cr.val)
            locate.next = node
            locate = node
            count += 1
            cr = cr.next
        #翻转片段尾端
        new_tail = ListNode(cr.val)
        add = new_tail
        while(count<n):
            cr = cr.next
            node = ListNode(cr.val)
            node.next = add
            add = node
            count += 1
        #翻转段结束
        locate.next = add
        cr = cr.next
        s = new_tail
        while cr:
            node = ListNode(cr.val)
            s.next = node
            s = s.next
            cr = cr.next

        return h.next    

# @lc code=end

