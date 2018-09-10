# 2_AddTwoNum (Medium)
# You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit. Add the two numbers and return it as a linked list.
# You may assume the two numbers do not contain any leading zero, except the number 0 itself.
'''Example 
Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)                << 數字相加，逐一標示出：個 -> 十 -> 百 >>
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.
'''
# ----------------------------------------------------------------------------------------------------------------
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode 2 4 3
        :type l2: ListNode 5 6 4
        :rtype: ListNode
        """
        carry = 0
        root = n = ListNode(0)      # ========      L: a -> b -> c -> Null (end)
        while l1 or l2 or carry:    # ListNode      n = L.val           n:a          n.next:b 
            v1 = v2 = 0             # ========      n.next.next : c     n.next.next.next = null
            if l1:                  #  (1)  (2)  (3)
                v1 = l1.val         #   2    4    3
                l1 = l1.next        # 2 -> 4 -> 3 -> null
            if l2:
                v2 = l2.val         #   5    6    4
                l2 = l2.next        # 5 -> 6 -> 4 -> null
            carry, val = divmod(v1+v2+carry , 10)   #(1) 2+5+0= 7, carry,val = 0,7
                                                    #(2) 4+6+0=10, carry,val = 1,0
                                                    #(3) 3+4+1= 8, carry,val = 0,8
            n.next = ListNode(val) # n:0->n.next:7  # n:7->n.next:0     #n:0->n.next:8
            n = n.next             # n:7            # n:0               #n:8  
        return root.next  #    0 -> 7 -> 0 -> 8 , 
                          # root:0,       n:8


if __name__ == '__main__':
    
    main()