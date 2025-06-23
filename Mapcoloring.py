regions = {
    'Andhra Pradesh': ['Telangana', 'Tamil Nadu', 'Karnataka', 'Odisha'],
    'Telangana': ['Andhra Pradesh', 'Karnataka', 'Maharashtra', 'Chhattisgarh'],
    'Karnataka': ['Goa', 'Maharashtra', 'Telangana', 'Andhra Pradesh', 'Tamil Nadu', 'Kerala'],
    'Tamil Nadu': ['Kerala', 'Karnataka', 'Andhra Pradesh', 'Puducherry'],
    'Kerala': ['Karnataka', 'Tamil Nadu'],
    'Goa': ['Karnataka'],
    'Puducherry': ['Tamil Nadu'],
    'Odisha': ['Andhra Pradesh', 'Chhattisgarh'],
    'Maharashtra': ['Karnataka', 'Telangana', 'Goa'],
    'Chhattisgarh': ['Telangana', 'Odisha']
}
colors = ['Red', 'Green', 'Blue', 'Yellow']
assignment = {}
def is_valid(region, color):
    for neighbor in regions[region]:
        if neighbor in assignment and assignment[neighbor] == color:
            return False
    return True
def backtrack():
    if len(assignment) == len(regions):
        return True
    unassigned = [r for r in regions if r not in assignment][0]
    for color in colors:
        if is_valid(unassigned, color):
            assignment[unassigned] = color
            if backtrack():
                return True
            del assignment[unassigned]
    return False
if backtrack():
    print("Color assignment for South Indian states:")
    for region in assignment:
        print(f"{region}: {assignment[region]}")
else:
    print("No valid coloring found.")