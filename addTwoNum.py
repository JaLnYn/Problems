class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def adder(self,n1,n2,n3):
        a = n1+n2+n3
        c = 0
        if a >= 10:
            a = a-10
            c = 1
        return (a,c)

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        cur1 = l1
        cur2 = l2

        a = self.adder(l1.val, l2.val, 0)
        prev_ans = ListNode(a[0])
        first_ans = prev_ans

        if cur1 is not None:
            cur1 = cur1.next

        if cur2 is not None:
            cur2 = cur2.next

        while (cur1 is not None or cur2 is not None or a[1]!= 0):
            
            x = 0
            y = 0
            if cur1 is not None:
                x = cur1.val
            if cur2 is not None:
                y = cur2.val

            a = self.adder(x,y,a[1])
            nnode = ListNode(a[0])
            prev_ans.next = nnode
            prev_ans = nnode
            if cur1 is not None:
                cur1 = cur1.next

            if cur2 is not None:
                cur2 = cur2.next

        return first_ans
