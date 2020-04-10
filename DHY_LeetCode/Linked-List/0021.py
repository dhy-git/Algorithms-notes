'''
合并两个有序链表
Category	Difficulty	Likes	Dislikes
algorithms	Easy (58.09%)	940	-

将两个升序链表合并为一个新的升序链表并返回。新链表是通过拼接给定的两个链表的所有节点组成的。 

示例：
输入：1->2->4, 1->3->4
输出：1->1->2->3->4->4
'''


# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        head = ListNode(None)
        head.next = l1
        pre = head
        cr1 = l1
        cr2 = l2
        
        while(cr1 and cr2 ):
            if(cr2.val >cr1.val):
                cr1 = cr1.next
                pre = pre.next
            else:
                temp = cr2.next

                pre.next = cr2
                cr2.next = cr1
                cr2 = temp

                pre = pre.next
        pre.next = cr1 if cr1 else cr2
        return head.next

# @lc code=end

'''
Accepted
208/208 cases passed (60 ms)
Your runtime beats 18.41 % of python3 submissions
Your memory usage beats 5 % of python3 submissions (13.7 MB)
'''