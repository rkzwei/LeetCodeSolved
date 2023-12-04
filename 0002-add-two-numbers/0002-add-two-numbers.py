# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
      
        result = ListNode(0) #initialize a linked list for our answer
        result_tail = result #initialize our worker list
        carry = 0 #initialize carrying var
        
        while l1 or l2 or carry: #True while True, since they'll run out of valid chars and return Null
            val1 = (l1.val if l1 else 0) #converts node to value if there is a value to be converted, else becomes 0 as to not influence operation
            val2 = (l2.val if l2 else 0) 
            carry, out = divmod(val1 + val2 + carry, 10) #sets carry as quotient and out as remainder of val1 and val2
            
            result_tail.next = ListNode(out) #sets the next node of tail as our remainder
            result_tail = result_tail.next #moves node along for next iteration
            
            l1 = (l1.next if l1 else None) #moves node along for next iteration, or None to end loop
            l2 = (l2.next if l2 else None)
            
        return result.next