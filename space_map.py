'''
space_map.py — Space Exploration Map Module

This module provides the core functionality for creating and managing a
space exploration map in the space exploration game. 

It allows users to initialise a map, display it and populate it with key 
entities including the ship, destination, hazards and waypoints.
'''


def create_map(n: int) -> list[list[str]]:
    # copy over from Operation 1
    grid = []
    for i in range(n):
        cell = [' '] * n
        grid.append(cell)
    return grid


def display_map(grid: list[list[str]]):
    # copy over from Operation 1
    for row in grid:
        row_str = '|'
        for cell in row:
            row_str += f' {cell} |'
        print(row_str)


def populate_map(grid: list[list[str]]):
    # copy over from Operation 1
# Place the ship
    grid[0][0] = '@'
    print("Placing: Ship")
    print("Ship placed: (0, 0)")
    display_map(grid)

# Place the destination
    print("\nPlacing: Destination")
    destination_status = True

    while destination_status:
        destination_cordinates = input("Enter (x y): ").strip().split()
        if len(destination_cordinates) == 2:
            cord_x = int(destination_cordinates[0])
            cord_y = int(destination_cordinates[1])
            if cord_x == 0 and cord_y == 0:
                print("Error: (0, 0) occupied by '@'")
            elif (not (0 <= cord_x < len(grid))) or (not (0 <= cord_y < len(grid))):
                print("Error: out of bounds")
            else:
                grid[cord_y][cord_x] = 'X'
                print(f"Destination placed: ({cord_x}, {cord_y})")
                display_map(grid)
                destination_status = False
        else:
            print("Error: expected <x> <y>")
            
#Placing Hazards and Waypoints
    print("\nPlacing: Hazards and Waypoints")
    symbol_dict = {'.' : 'Asteroid', 'E' : 'Enemy', 'M' : 'Mineral', 'R' : 'Repair Station'}
    hazard_status = True

    while hazard_status:
        hazard_waypoints_cordinates = input("Enter (symbol x y | display | done): ").strip().split()
        if len(hazard_waypoints_cordinates) == 1:
            if hazard_waypoints_cordinates[0] == "display":
                display_map(grid)
            elif hazard_waypoints_cordinates[0] == "done": 
                display_map(grid)
                hazard_status = False
            else:
                print("Error: expected <symbol> <x> <y>") 
        elif len(hazard_waypoints_cordinates) == 3:
            symbol = hazard_waypoints_cordinates[0]
            symbol_x = int(hazard_waypoints_cordinates[1])
            symbol_y = int(hazard_waypoints_cordinates[2])
            if symbol not in symbol_dict:
                print(f"Error: '{symbol}' not recognised")
            elif (not (0 <= symbol_x < len(grid))) or (not (0 <= symbol_y < len(grid))):
                print("Error: out of bounds")
            elif grid[symbol_y][symbol_x] != " ":
                print(f"Error: ({symbol_x}, {symbol_y}) occupied by '{grid[symbol_y][symbol_x]}'")
            else:
                grid[symbol_y][symbol_x] = symbol
                print(f"{symbol_dict[symbol]} placed: ({symbol_x}, {symbol_y})")
        else:
            print("Error: expected <symbol> <x> <y>") 


if __name__ == '__main__':
    # you can put any test code here!
    # this only runs when its the main program ran i.e. python3 space_map.py
    pass
