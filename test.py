#-*- coding:utf-8 -*-
# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        if not l1 and not l2: return
        result = ListNode(0)
        l = result
        while l1 and l2:
            if l1.val < l2.val:
                l.next = l1
                l1 = l1.next
            else:
                l.next = l2
                l2 = l2.next
            # 融合後連結串列的下一位,當前位置剛剛賦值
            l = l.next
        # 把剩餘的連結串列排在後面
        l.next = l1 or l2
        # 返回融合後連結串列從第二個物件開始，第一個物件是自己建立的ListNode(0)
        return result.next


if __name__ == '__main__':
    # 建立l1和l2兩個連結串列，注意，排序好的就需要arr1和arr2中數字從小到大
    # arr1 = [1, 2, 3]
    # arr2 = [5, 6, 7]
    arr1 = list(input())
    arr2 = list(input())
    l1 = ListNode(arr1[0])
    p1 = l1
    l2 = ListNode(arr2[0])
    p2 = l2
    for i in arr1[1:]:
        p1.next = ListNode(i)
        p1 = p1.next
    for i in arr2[1:]:
        p2.next = ListNode(i)
        p2 = p2.next
    s = Solution()
    # 融合兩個連結串列
    q = s.mergeTwoLists(l1, l2)
    L =[]
    n = q
    if n:
        a = n.val
        print(a)
        L.append(a)
        n = n.next

    print(L,q.val,q.next.val)

    a = p1.next
    
    print('l1:',type(p1))