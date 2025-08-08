
# need attention


class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:
        dummy = ListNode(0, head)
        fast = dummy
        slow = dummy
        
        # move fast ahead by n steps
        for _ in range(n):
            fast = fast.next
            
        # Move both pointers until fast reaches the end
        while fast.next:
            fast = fast.next
            slow = slow.next
            
        # skip the target node
        slow.next = slow.next.next
        
        return dummy.next
    
    
    # Approach: Two Pointer Technique
    """
    Idea:
Use two pointers, fast and slow.

Steps:
Move fast n steps ahead

Now move fast and slow together until fast hits the end

Now, slow is at the node just before the one we want to remove

Skip the next node: slow.next = slow.next.next
    """
    
"""
🔓 Summary (Memory Trigger)
Move fast ahead n steps → maintain distance
Move both together until fast.next = None
Now slow is exactly before the node to remove → delete it.

"""

