1.
```
if not l1 and not l2:
return []
```
This is so much cleaner...
```
if l1 is None:
return l2
elif l2 is None:
return l1
```
​
​
​
---
1/12/23 -- Prev Accepted:
`# Definition for singly-linked list.`
`# class ListNode:`
`#     def __init__(self, val=0, next=None):`
`#         self.val = val`
`#         self.next = next`
`class Solution:
def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
# For Edge Cases
dummy = ListNode()
tail = dummy
while list1 and list2:
if list1.val < list2.val:
tail.next = list1
list1 = list1.next
else:
tail.next = list2
list2 = list2.next
tail = tail.next
if not list1:
tail.next = list2
elif not list2:
tail.next = list1
return dummy.next#return tail`