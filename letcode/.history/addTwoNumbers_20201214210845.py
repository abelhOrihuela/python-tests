class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        output = []
        carrie = 0
        while l1 or l2 or carrie:
            
            sum = int(l1.val) + int(l2.val) + carrie
            
            carrie, out = divmod(sum, 10)
            
            if carrie > 0:
                sum = out
                
            output.append(sum)



soluction = Solution()
soluction.addTwoNumbers(
    ListNode([2,4,3]),
    ListNode([5,6,4])
)