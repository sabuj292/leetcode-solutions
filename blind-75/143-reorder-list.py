# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next



# need further attention
# go deeper and understand the logic 

def reorderList(head):
    # if the list is empty(None) or has only one node, there's nothing to reorder, so we just return
    
    # Step-0: handle tiny lists
    if not head or not head.next:
        return
    
    # step-1: finding the middle
    # called "Tortoise and Hare" technique
    # slow: moves one step at a time
    # fast: moves two step at a time
    # when fast reaches the end, slow is in the middle of the list
    # Why: because fast moves twice as fast, it reaches the end while slow is halfway
    
    """
    1 → 2 → 3 → 4 → 5
    ↑         ↑
  slow      fast

    """
   
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        
    
    # Step-2: Reverse the second half
    """
    We're about to reverse the second half of the list
    we cut the list into two parts:
        First half: head -> -------- -> slow
        Second half: slow.next -> ----- -> end
        
    so we set slow.next = None to disconnect them
    """
    
    
    prev = None
    curr = slow.next
    slow.next = None # cut the first half
    while curr:
        next_node = curr.next
        curr.next = prev
        prev = curr
        curr = next_node
        
    # merge the two halves
    
    """
    first: points to the start of the first half (1 > 2 > 3)
    second: points to the start of the reversed second half (5 > 4)
    """
    first, second = head, prev
    while second:
        tmp1, tmp2 = first.next, second.next
        first.next = second
        second.next = tmp1
        first = tmp1
        second = tmp2
        
        
        
# Summary Table::
"""
    1. Find Middle: Use fast and slow pointer to split in half
    2. Reverse Half: Reverse second half of the list
    3. Merge Halves: Interleave nodes from first and second
"""

# Key Insights

"""
We do not modify values in nodes
we do not touch the content of the first half directly
But we interleave the reversed second half Into the first half:
    That's why the first half only "looks untouched"
        But during merging, we stitch together alternating nodes from 
            First half (L0, L1, L2, ...)
            Reversed second half (Ln, Ln-1, ...)
        Then:
            We pick one from the first half, one from the second half (reversed), and link them in order, one by one.
"""