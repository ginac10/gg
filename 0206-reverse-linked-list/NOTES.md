newLList = []
prev = [head.val]
temp = []
while head.next: #while there is a next,
temp = head.next.next
head.next
try 2:
newL = head
temp = newL
while temp != None:
newL = head.next
temp = newL.next
newL.next = head
head.next = None
head = newL