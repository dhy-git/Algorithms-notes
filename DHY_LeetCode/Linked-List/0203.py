
# [203] 移除链表元素
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def removeElements(self, head: ListNode, val: int) -> ListNode:
        p = head
        #修改头
        while p != None and p.val == val:
            p = p.next 
            head = p
        #遍历链表 搜索 断开 重连
        while(p != None):
            while p.next != None and  p.next.val == val:
                p.next = p.next.next
            p = p.next
        return head


# @lc code=end

