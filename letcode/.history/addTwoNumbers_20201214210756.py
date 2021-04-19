class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        
        sum = 5 + 5

        q, r = divmod(sum, 10)

        print(q, r)



soluction = Solution()
soluction.addTwoNumbers(
    ListNode([2,4,3]),
    ListNode([5,6,4])
)