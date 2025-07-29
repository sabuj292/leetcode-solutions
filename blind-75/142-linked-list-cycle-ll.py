

# using Floyd's algorithm

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        # Step 1: Detect if a cycle exists
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:  # cycle detected
                break
        else:
            return None  # no cycle
        # Step 2: Move one pointer to head, keep other at meeting point
        slow = head
        # Step 3: Move both 1 step at a time
        while slow != fast:
            slow = slow.next
            fast = fast.next
        return slow  # the start of the cycle



# using hashing 
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def detectCycle(self, head):
        visited = set()
        current = head
        
        while current:
            if current in visited:
                return current
            visited.add(current)
            current = current.next()
            
        return None
                