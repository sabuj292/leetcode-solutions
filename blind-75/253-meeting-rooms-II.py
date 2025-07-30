""""
### ✅ Short Summary:

You're given a list of meeting time intervals, and you need to **find the minimum number of conference rooms** required so that **no two meetings overlap**.

### Key Idea:

* If one meeting starts **before** another ends, they **need separate rooms**.
* Otherwise, a room can be **reused**.

### Optimal Approach:

1. **Sort** start and end times separately.
2. Use two pointers to **track overlaps**.
3. Count how many rooms are needed at the **maximum overlap**.

🟩 **Goal:** Return the **maximum number of rooms** needed at any time.


"""



"""
    You're working on a classic **Interval Scheduling** problem—commonly referred to as **"Meeting Rooms II"**.

---

### 🔍 Problem Breakdown

#### 🧠 **Objective**:

Given a list of intervals where each interval represents a meeting (`[start, end]`), **find the minimum number of conference rooms** required so that **no meetings overlap**.

---

### 📥 Input:

A list of intervals, each in the form:

```
intervals = [[start1, end1], [start2, end2], ..., [startN, endN]]
```

---

### 📤 Output:

An integer representing the **minimum number of rooms** required.

---

### 📘 Constraints:

* `1 <= intervals.length <= 10^4`
* `0 <= starti < endi <= 10^6`

---

### 🧠 Understanding Through Examples:

#### ✅ Example 1:

```python
intervals = [[0,30],[5,10],[15,20]]
```

* Meeting 1: 0 → 30
* Meeting 2: 5 → 10
* Meeting 3: 15 → 20

Here’s the time overlap:

* 0–30 overlaps with 5–10 (need **2 rooms**).
* 15–20 also overlaps with 0–30 (still **2 rooms** needed).
  🟩 **Answer: 2**

---

#### ✅ Example 2:

```python
intervals = [[7,10],[2,4]]
```

* Meeting 1: 7 → 10
* Meeting 2: 2 → 4

No overlap at all.
🟩 **Answer: 1**

---

### 💡 Core Insight:

You **only need a new room** if a meeting starts **before** the previous one ends.

---

### ✅ Strategy to Solve:

#### Option 1: **Two-Pointer + Sorting**

1. **Extract start and end times** into two separate arrays.
2. **Sort** both arrays.
3. Use two pointers:

   * Iterate through each start time.
   * Compare it with the earliest end time.
   * If the start is before the end → **need new room**.
   * Else → **reuse the room**.

**Time Complexity**: O(n log n)
**Space Complexity**: O(n)

---

### ✅ Visual Aid:

```
Start times: [0, 5, 15]
End times:   [10, 20, 30]

Compare:
start[0] = 0 < end[0] = 10 → +1 room
start[1] = 5 < end[0] = 10 → +1 room
start[2] = 15 > end[0] = 10 → reuse room, move end ptr
```

🟩 Max rooms used simultaneously = 2

---

Would you like the full code implementation and step-by-step trace with this logic?

"""




# Final logic  break down
"""
💡 Final Thought:
        You're always asking:
            “Does the next meeting start before any meeting ends?”

                1) Yes → Need extra room

                2) No → Can reuse a room
"""


def minMeetingRooms(intervals):
    if not intervals:
        return 0
    
    # Extract start and end times
    starts = sorted(i[0] for i in intervals)
    ends = sorted(i[1] for i in intervals)
        
    # pointers for start and end times
    
    s_ptr, e_ptr = 0, 0
    used_rooms = 0
    max_rooms = 0
    
    while s_ptr < len(intervals):
        if starts[s_ptr] < ends[e_ptr]:
            # need a new room
            used_rooms += 1
            s_ptr += 1
        else:
            # one meeting ended reuse the room
            used_rooms -= 1
            e_ptr += 1
    
    max_rooms = max(max_rooms, used_rooms)
    
    
    return max_rooms

print(minMeetingRooms([[0,30],[5,10],[15,20]]))  # Output: 2
print(minMeetingRooms([[7,10],[2,4]]))           # Output: 1
