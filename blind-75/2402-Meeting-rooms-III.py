import heapq

def mostBooked(n, meetings):
    # Step 1: Sort meetings by start time
    meetings.sort()
    
    # Step 2: Initialize heaps and counters
    available_rooms = list(range(n))  # min-heap for free rooms
    heapq.heapify(available_rooms)
    
    busy_rooms = []  # min-heap of (end_time, room)
    room_meeting_count = [0] * n
    
    for start, end in meetings:
        # Step 3: Free up rooms whose meetings have ended
        while busy_rooms and busy_rooms[0][0] <= start:
            end_time, room = heapq.heappop(busy_rooms)
            heapq.heappush(available_rooms, room)
        
        # Step 4: Assign room
        if available_rooms:
            room = heapq.heappop(available_rooms)
            heapq.heappush(busy_rooms, (end, room))
        else:
            end_time, room = heapq.heappop(busy_rooms)
            delay = end - start
            new_end = end_time + delay
            heapq.heappush(busy_rooms, (new_end, room))
        
        # Step 5: Update count
        room_meeting_count[room] += 1

    # Step 6: Find room with max meetings (smallest index if tie)
    max_meetings = max(room_meeting_count)
    for i in range(n):
        if room_meeting_count[i] == max_meetings:
            return i


print(mostBooked(2, [[0,10],[1,5],[2,7],[3,4]]))  # Output: 0
print(mostBooked(3, [[1,20],[2,10],[3,5],[4,9],[6,8]]))  # Output: 1
