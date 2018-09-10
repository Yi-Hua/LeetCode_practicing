# 21 Merge Two Sorted Lists 合併兩個排序列表 (Easy)  ✓
# Merge two sorted linked lists and return it as a new list. 
# The new list should be made by splicing together the nodes of the first two lists.
'''
Input: 1->2->4, 1->3->4             << 合併兩個列表，並排序 >>
Output: 1->1->2->3->4->4
'''

class ListNode:                     # Definition for singly-linked list.
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        dummy = cur = ListNode(0)
        while l1 and l2:            # l1: 1 -> 2 -> 4 , l2: 1 -> 3 -> 4
            if l1.val < l2.val:     # 1) l1.val = 1 = l2.val,     False: cur.next = l2 = 1, l2 = l2.next = 3  
                cur.next = l1       # 2) l1.val = 1 < 3 = l2.val,  True: cur.next = l1 = 1, l1 = l1.next = 2      
                l1 = l1.next        # 3) l1.val = 2 < 3 = l2.val,  True: cur.next = l1 = 2, l1 = l1.next = 4     
            else:                   # 4) l1.val = 4 > 3 = l2.val, False: cur.next = l2 = 3, l2 = l2.next = 4   
                cur.next = l2       # 4) l1.val = 4 = l2.val,     False: cur.next = l2 = 4, l2 = l2.next = None    
                l2 = l2.next        # cur = cur.next = None    
            cur = cur.next           
        cur.next = l1 or l2 
                
        return dummy.next.val         
        
    
if __name__ == '__main__':
    s1 = ListNode(input())
    s2 = ListNode(input())
    sol = Solution()
    print(sol.mergeTwoLists(s1,s2))
     



