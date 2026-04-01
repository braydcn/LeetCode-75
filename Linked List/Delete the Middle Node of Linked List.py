# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        size = 0
        sizecheck = head
        while sizecheck != None:
            size += 1
            sizecheck = sizecheck.next

        if size == 0 or size == 1:
            return None

        middle = size//2
        current = head

        for i in range(middle - 1):
            current = current.next
        current.next = current.next.next
        return head