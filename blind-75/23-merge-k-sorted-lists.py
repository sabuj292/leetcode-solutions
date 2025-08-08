"""
🔑 Efficient Solution: Use a Min-Heap
✅ Why heap?
Each list is already sorted.

So the first node of each list is the smallest available in that list.

To get the globally smallest value across all lists, use a min-heap of the first node of each list.
"""

"""
🧠 High-Level Algorithm:
    Initialize a min-heap.

    Push the first node of each list into the heap.

    While the heap is not empty:

        Pop the smallest node.

        Append it to the result list.

        If the popped node has a next node, push it into the heap.

Return the merged linked list.
"""

import heapq

class ListNode:
    def __init__(self, val = 0, next = None):
        self.val = val
        self.next = next
        
    def __lt__(self, other):
        return self.val < other.val # for heapq to compare nodes
    
    
def mergeKLists(lists):
    heap = []
    
    # Step-1: put the first node of each list into the heap
    for i, node in enumerate(lists):
        if node:
            heapq.heappush(heap, node)
            
    dummy = ListNode(0)
    tail = dummy
    
    # Step-2: Pop the smallest and add next from that list
    # build result list
    
    while heap:
        smallest= heapq.heappop(heap)
        tail.next = smallest
        tail = tail.next
        
        if smallest.next:
            heapq.heappush(heap, smallest.next)
            
        return dummy.next
    
    
    
    
    
# For leetcode 

import heapq
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional['ListNode']]) -> Optional['ListNode']:
        heap = []

        # Step 1: Push (val, index, node) for each non-empty list
        for idx, node in enumerate(lists):
            if node:
                heapq.heappush(heap, (node.val, idx, node))

        dummy = ListNode(0)
        tail = dummy

        while heap:
            val, idx, node = heapq.heappop(heap)
            tail.next = node
            tail = tail.next

            if node.next:
                heapq.heappush(heap, (node.next.val, idx, node.next))

        return dummy.next


"""
🧠 First, Why We Use Tuples: (val, index, node)
🧨 Problem:
    Python can’t compare two ListNode objects unless we define __lt__.

    But in online judges (like LeetCode), we can’t change their ListNode class.
    
    
    
✅ Solution:
Use a tuple like this:

    (node.val, index, node)
    
    val: used for sorting (min-heap).

index: used to break ties if two nodes have the same val.

node: the actual ListNode we’re merging into the result.

       1) node.val is the value we care about (used for sorting).

        2) index is a unique number, added to avoid a tie.

        3) node is the actual ListNode (we still need it).
        

Python can always compare two tuples if:

    1) The first element is comparable (like an integer)

    2) If values are equal, the second item (index) will break the tie

"""
    
# Simulation How the Codes Work (you are gonna love it)::
 
"""
We'll simulate each iteration of the heap popping and building the result list.

Initial Input Lists:
"""

"""
| List # | Linked List |
| ------ | ----------- |
| 0      | 1 → 4 → 5   |
| 1      | 1 → 3 → 4   |
| 2      | 2 → 6       |

"""
"""
# most exciting part: Step-by-Step Simulation

| Step | Heap Before| Node Popped | Result List So Far            | Heap After (Next Pushed)     |
| ---- | -----------  ----------- | ----------------------------- | -----------------------------|
| 0    | -          | -           | -                             | Push [1, 1, 2]               |
| 1    | [1, 1, 2]  | 1 (from L0) | 1                             | Push 4 (from L0) → [1, 2, 4] |
| 2    | [1, 2, 4]  | 1 (from L1) | 1 → 1                         | Push 3 (from L1) → [2, 4, 3] |
| 3    | [2, 4, 3]  | 2 (from L2) | 1 → 1 → 2                     | Push 6 (from L2) → [3, 4, 6] |
| 4    | [3, 4, 6]  | 3 (from L1) | 1 → 1 → 2 → 3                 | Push 4 (from L1) → [4, 6, 4] |
| 5    | [4, 6, 4]  | 4 (from L0) | 1 → 1 → 2 → 3 → 4             | Push 5 (from L0) → [4, 6, 5] |
| 6    | [4, 6, 5]  | 4 (from L1) | 1 → 1 → 2 → 3 → 4 → 4         | No push (L1 ends) → [5, 6]   |
| 7    | [5, 6]     | 5 (from L0) | 1 → 1 → 2 → 3 → 4 → 4 → 5     | No push (L0 ends) → [6]      |
| 8    | [6]        | 6 (from L2) | 1 → 1 → 2 → 3 → 4 → 4 → 5 → 6 | No push (L2 ends) → []       |



🔚 Final Result:

Merged Linked List:
1 → 1 → 2 → 3 → 4 → 4 → 5 → 6

"""

# 📌 Heap Content as a Snapshot

"""
[1, 1, 2] → pop 1
[1, 2, 4] → pop 1
[2, 4, 3] → pop 2
[3, 4, 6] → pop 3
[4, 6, 4] → pop 4
[4, 6, 5] → pop 4
[5, 6]    → pop 5
[6]       → pop 6
[]        → Done!


"""

# Summary::

"""
| Concept             | Explanation                                            |
| ------------------- | ------------------------------------------------------ |
| Heap Initialization | Push first node of each list                           |
| Core Operation      | Pop smallest, add to result, push `.next`              |
| Key Advantage       | Always deal with smallest node → result list is sorted |
| Time Complexity     | O(N log k)                                             |

"""

    
"""
for i, node in enumerate(lists):
    if node:
        heapq.heappush(heap, node)

"""
# Explanation::

"""
lists = [
    1 → 4 → 5,
    1 → 3 → 4,
    2 → 6
]

It’s a list of ListNode heads. 

So:

    lists[0] is a ListNode pointing to 1 → 4 → 5

    lists[1] is a ListNode pointing to 1 → 3 → 4

    lists[2] is a ListNode pointing to 2 → 6

All of these are just references to the head of each linked list.

Loop: for i, node in enumerate(lists):
This loop goes through the list of linked lists one by one.

i = 0 → node = lists[0] → node.val = 1
i = 1 → node = lists[1] → node.val = 1
i = 2 → node = lists[2] → node.val = 2

✅ Check: if node:
If the list is not empty (some lists could be None), we move ahead.

📥 heapq.heappush(heap, node)
We push the current ListNode into the heap.

So the heap now contains:

heap = [
    ListNode(1),  # from lists[0]
    ListNode(1),  # from lists[1]
    ListNode(2)   # from lists[2]
]

The heap does not push all the nodes, only the first node of each list.


🔧 How It Uses These First Nodes
These first nodes are representatives of each list. Why?

Because:

Since each list is already sorted, the first node is the smallest in its own list.

By putting all the first nodes in the heap, you are saying:

"Hey heap, tell me the smallest node among all these first ones."

Heap will give you:

1 → the smallest among 1, 1, and 2.

Then you:

Pop that 1 out of the heap.

Go to its .next (e.g. 4), and push that into the heap.

So now you’re saying:

“Hey heap, now tell me the smallest among the new first nodes.”


"""


# __lt__:
"""
__lt__ means "less than"

    it is a special funtion inside a class that tells python how to compare two objects using "<"


🤖 Why do we need it?
Python knows how to compare numbers:
2 < 5  # True



But Python does NOT know how to compare objects like:

node1 < node2  # ❌ ERROR!
Because:

Python says: “Hey, what does < even mean for these nodes?”

So you have to teach Python:

"When comparing two nodes, look at their .val and use that."



✅ That’s where __lt__ helps
You define this in your class:

def __lt__(self, other):
    return self.val < other.val
Now Python understands:


node1 < node2  →  node1.val < node2.val

"""