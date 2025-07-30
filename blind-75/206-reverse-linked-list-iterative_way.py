# For leetcode 
# method - iterative
# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        prev = None
        curr = head
        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        return prev














# Node definition
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

# Function to reverse linked list with debug print
def reverseList(head):
    prev = None
    curr = head
    step = 0

    print("\n--- Reversing Process Begins ---\n")
    while curr:
        print(f"Step {step}:")
        print(f"  Current Node: {curr.val}")
        if curr.next:
            print(f"  Next Node: {curr.next.val}")
        else:
            print(f"  Next Node: None")
        if prev:
            print(f"  Previous Node: {prev.val}")
        else:
            print(f"  Previous Node: None")

        next_node = curr.next        # Save next
        curr.next = prev             # Reverse pointer
        prev = curr                  # Move prev forward
        curr = next_node             # Move curr forward

        step += 1
        print_linked_list(prev, label="  Partial Reversed List")

    print(f"\n--- Reversing Complete ---")
    print(f"New Head: {prev.val if prev else 'None'}\n")
    return prev

# Helper to build linked list from list
def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

# Helper to print linked list
def print_linked_list(head, label="List"):
    print(f"{label}: ", end="")
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# ----------------------------
#  Test Cases
# ----------------------------

# Test 1: [1, 2, 3, 4, 5]
head1 = build_linked_list([1, 2, 3, 4, 5])
print("Original List:")
print_linked_list(head1)

reversed_head1 = reverseList(head1)

print("Reversed List:")
print_linked_list(reversed_head1)

# Test 2: [1, 2]
head2 = build_linked_list([1, 2])
print("\nOriginal List:")
print_linked_list(head2)

reversed_head2 = reverseList(head2)

print("Reversed List:")
print_linked_list(reversed_head2)

# Test 3: []
head3 = build_linked_list([])
print("\nOriginal List:")
print_linked_list(head3)

reversed_head3 = reverseList(head3)

print("Reversed List:")
print_linked_list(reversed_head3)
