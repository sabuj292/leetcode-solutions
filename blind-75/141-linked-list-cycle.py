# easiest way using set

class Solution(object):
    def hasCycle(self, head):
        visited = set()
        current = head

        while current:
            if current in visited:
                return True
            visited.add(current)
            current = current.next

        return False


# we can also use List instead of set in that case it will increase the run time whereas set gives us around 40ms and while using list it will be over 2000 ms run time





# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def hasCycle(self, head):
        slow = head          # step 1: start both at head
        fast = head

        while fast and fast.next:   # step 2: check bounds
            slow = slow.next        # step 3: move slow by 1
            fast = fast.next.next   # step 4: move fast by 2

            if slow == fast:        # step 5: if they meet, cycle
                return True

        return False                # step 6: if fast hits end, no cycle

# Floy's cycle detection algorithm need to understand the algorithm

