# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """
        # 1. Find the midpoint using fast/slow pointers. O(n)
        fast = head.next#.next ## Bc if next is None, cannot do .next.next
        slow = head
        while fast and fast.next:## and fast.next bc None cannot have .next
            slow = slow.next
            fast = fast.next.next

        new = slow.next
        prev = slow.next = None ## (added the prev)
        # head and new are your LNs
        
        # 2. Reverse the 2nd LN (new)
        ##prev = ListNode(None)
        ##nxt = new.next
        ##curr = prev
        while new:
            nxt = new.next ##
            new.next = prev##curr
            prev = new
            new = nxt
        
        ##prev = prev.next ## Don't need to do bc prev set to None, not LN(None)
        #prev is the new list
        
        # 3. Put it all together
        first, second = head, prev
        
        while second:
            t1, t2 = first.next, second.next
            first.next = second
            second.next = t1
            first, second = t1, t2
        
            ##first = t1
            ##second.next = first
            ##second = t2