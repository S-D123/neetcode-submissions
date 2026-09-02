# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        arr = [0] * 1000
        ptr = head
        i = 0

        while ptr:
            arr[i] = ptr.val
            ptr = ptr.next
            i += 1

        ptr = head
        for j in range(i-1, -1, -1):
            ptr.val = arr[j]
            ptr = ptr.next

        return head
        