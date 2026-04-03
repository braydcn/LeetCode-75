# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def pairSum(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: int
        """
        current = head
        arraylist = []
        size = 0
        while current != None:
            arraylist.append(current.val)
            current = current.next
            size += 1
        maxnum = 0
        for i in range(len(arraylist)//2):
           if arraylist[i] + arraylist[size - 1 - i] > maxnum:
            maxnum = arraylist[i] + arraylist[size - 1 - i]
        return maxnum
