class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, list1, list2):
        dummy = ListNode(-1)
        current = dummy

        while list1 and list2:
            if list1.val < list2.val:
                current.next = list1
                list1 = list1.next
            else:
                current.next = list2
                list2 = list2.next
            current = current.next

        if list1:
            current.next = list1
        if list2:
            current.next = list2

        return dummy.next

# -------------------
# Helper Functions
# -------------------

# Converts Python list -> Linked List
def build_linked_list(values):
    dummy = ListNode()
    current = dummy
    for val in values:
        current.next = ListNode(val)
        current = current.next
    return dummy.next

# Converts Linked List -> Python list
def linked_list_to_list(node):
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result

# -------------------
# Main Test Code
# -------------------

if __name__ == "__main__":
    list1 = build_linked_list([1, 2, 4])
    list2 = build_linked_list([1, 3, 4])

    solution = Solution()
    merged = solution.mergeTwoLists(list1, list2)

    print("Merged List:", linked_list_to_list(merged))
    
    
    
# another way with better run time

# Definition for singly-linked list.
class ListNode(object):
     def __init__(self, val=0, next=None):
         self.val = val
         self.next = next
         
# no need the following "addNode function"
def addNode(head, added):
    while(head.next!=None):
        head = head.next
    head.next = added
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        """
        :type list1: Optional[ListNode]
        :type list2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        if not list1:
            return list2
        if not list2:
            return list1
        #set head and tail node
        if list1.val>list2.val:
            head=tail=list2
            list2 = list2.next
        else:
            head=tail=list1
            list1 = list1.next
        while(list1 and list2):
            if(list1.val>list2.val):
                tail.next=list2
                tail=list2
                list2=list2.next
            else:
                tail.next=list1
                tail=list1
                list1=list1.next
        #attach leftover nodes        
        if list1:
            tail.next = list1
        else:
            tail.next=list2
        return head
        
        #loop until one or both lists are empty(.next is null), add the rest of the remaining array onto the end
        #
        
