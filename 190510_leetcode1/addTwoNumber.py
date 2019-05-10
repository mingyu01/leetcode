class ListNode:
    def __init__(self, x, _next = None):
        self.val = x
        self.next = _next


class Solution:
    def addTwoNumber(self, l1:ListNode, l2:ListNode) -> ListNode:
        self.l1 = l1
        self.l2 = l2
        targetList = None
        temp = []

        data_carry = 0
        while l1 != None and  l2 != None:
            data_sum = (l1.val + l2.val + data_carry) % 10
            data_carry = (l1.val + l2.val + data_carry) // 10
            temp.append(data_sum)
            l1 = l1.next
            l2 = l2.next
        
        while l1 != None:
            data_sum = (l1.val + data_carry) % 10
            data_carry = (l1.val + data_carry) // 10
            temp.append(data_sum)
            l1 = l1.next 
        
        while l2 != None:
            data_sum = (l2.val + data_carry) % 10
            data_carry = (l2.val + data_carry) // 10
            temp.append(data_sum)
            l2 = l2.next
    
        if data_carry != 0:
            temp.append(data_carry)
            
        for i in range(len(temp)):
            targetList = ListNode(temp[-i-1], targetList)
        
        return targetList


if __name__ == '__main__':
    ln1 = ListNode(3, None)
    ln1 = ListNode(4, ln1)
    ln1 = ListNode(2, ln1)
    # ln1 = ListNode(7, ln1)
    # ln1 = ListNode(8, ln1)
    # ln1 = ListNode(9, ln1)

    ln2 = ListNode(4, None)
    ln2 = ListNode(6, ln2)
    ln2 = ListNode(5, ln2)
    # ln2 = ListNode(7, ln2)
    # ln2 = ListNode(8, ln2)
    # ln2 = ListNode(9, ln2)

    sol = Solution()
    s = sol.addTwoNumber(ln1, ln2)

    print('input1 = ', end = '')
    while ln1 != None:
        print(ln1.val, end = '')
        ln1 = ln1.next
    print()

    print('input2 = ', end = '')
    while ln2 != None:
        print(ln2.val,end = '')
        ln2 = ln2.next
    print()

    print('output = ', end = '')
    while s != None:
        print(s.val, end = '')
        s = s.next
    print()