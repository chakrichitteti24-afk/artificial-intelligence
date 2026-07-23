"""
Experiment 09: Meeting Scheduling
Objective: Implement a simple meeting scheduling constraint satisfaction problem.
"""

def schedule_meetings(meetings, rooms):
    """
    Schedules a list of meetings into a list of rooms using a greedy approach.
    meetings: list of tuples (meeting_name, start_time, end_time)
    rooms: list of room names
    """
    schedule = {}
    # Sort meetings by their end time to maximize the number of meetings we can schedule
    meetings.sort(key=lambda x: x[2])
    
    for m in meetings:
        placed = False
        for r in rooms:
            if is_available(schedule.get(r, []), m):
                if r not in schedule:
                    schedule[r] = []
                schedule[r].append(m)
                placed = True
                break
        if not placed:
            print(f"Could not schedule meeting {m[0]} due to room unavailability.")
    return schedule

def is_available(room_meetings, new_meeting):
    """
    Checks if a new meeting can be added to the room's current schedule without overlapping.
    """
    for m in room_meetings:
        # Check for time overlap
        if max(m[1], new_meeting[1]) < min(m[2], new_meeting[2]):
            return False
    return True

if __name__ == "__main__":
    meetings = [
        ("M1", 9, 10),
        ("M2", 9, 11),
        ("M3", 10, 12),
        ("M4", 11, 13),
        ("M5", 10, 11)
    ]
    rooms = ["Room A", "Room B"]
    
    print("Scheduling Meetings...")
    schedule = schedule_meetings(meetings, rooms)
    
    print("\nFinal Schedule:")
    for room, meets in schedule.items():
        print(f"{room}:")
        for m in meets:
            print(f"  {m[0]} from {m[1]}:00 to {m[2]}:00")
