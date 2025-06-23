# Initial State: (Position, Room A status, Room B status)
# Position: 'A' or 'B'; Status: 'Clean' or 'Dirty'
position = 'A'
roomA = 'Dirty'
roomB = 'Dirty'

# Environment steps
print("Initial State:")
print(f"Vacuum at: {position}, Room A: {roomA}, Room B: {roomB}\n")

# Agent's decision-making loop
while roomA == 'Dirty' or roomB == 'Dirty':
    if position == 'A':
        if roomA == 'Dirty':
            print("Cleaning Room A")
            roomA = 'Clean'
        else:
            print("Moving to Room B")
            position = 'B'
    elif position == 'B':
        if roomB == 'Dirty':
            print("Cleaning Room B")
            roomB = 'Clean'
        else:
            print("Moving to Room A")
            position = 'A'
    print(f"Vacuum at: {position}, Room A: {roomA}, Room B: {roomB}\n")

print("Both rooms are clean. Goal achieved!")