'''
>>>合并K个排序链表
    Category	Difficulty	Likes	Dislikes
    algorithms	Hard (47.78%)	565	-
    合并 k 个排序链表，返回合并后的排序链表。请分析和描述算法的复杂度。

    示例:
    输入:
    [
    1->4->5,
    1->3->4,
    2->6
    ]
    输出: 1->1->2->3->4->4->5->6
'''


# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

from typing import List
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None
class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        if(not lists):
            return []
        while(len(lists)>1):
            l1 = lists.pop(0)
            l2 = lists.pop(0)
            lists.append(self.mergeTwoLists(l1,l2))
        return lists[0]

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
131/131 cases passed (104 ms)
Your runtime beats 69.64 % of python3 submissions
Your memory usage beats 31.01 % of python3 submissions (16.6 MB)

复杂度O(n) n=链表总长
'''