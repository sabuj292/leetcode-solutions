# the main function only for leetcode
# Definition for singly-linked list.
# 
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# class Solution(object):
#     def reverseList(self, head):
#         """
#         :type head: Optional[ListNode]
#         :rtype: Optional[ListNode]
#         """
#         if not head or not head.next:
#             return head
#         # recurse till tail
#         new_head = self.reverseList(head.next)
#         # reverse the link
        # head.next.next = head     "core of the the method"
#         head.next = None

#         return new_head



# printable 

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

def reverseListRecursive(head, depth=0):
    indent = "  " * depth

    if not head:
        print(f"{indent}Reached end (None)")
        return None

    if not head.next:
        print(f"{indent}Base case reached: {head.val}")
        return head

    print(f"{indent}Calling reverse on: {head.val} -> {head.next.val}")

    new_head = reverseListRecursive(head.next, depth + 1)

    print(f"{indent}Reversing: {head.next.val} -> {head.val}")
    head.next.next = head
    head.next = None

    return new_head

def build_linked_list(values):
    if not values:
        return None
    head = ListNode(values[0])
    current = head
    for val in values[1:]:
        current.next = ListNode(val)
        current = current.next
    return head

def print_linked_list(head, label="List"):
    print(f"{label}: ", end="")
    while head:
        print(head.val, end=" -> ")
        head = head.next
    print("None")

# Test
head = build_linked_list([1, 2, 3, 4, 5])
print("Original List:")
print_linked_list(head)

print("\n--- Recursive Reversal Begins ---")
reversed_head = reverseListRecursive(head)

print("\nReversed List:")
print_linked_list(reversed_head)
