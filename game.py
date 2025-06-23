'''
game.py — Space Exploration Game Module

The game module runs the space exploration game.

It coordinates gameplay by integrating the map functionality from space_map.py
and the Ship class from ship.py. This module initialises the space exploration
map and ship, and runs the game where players issue commands to explore the 
map, interact with entities, and aim to reach the destination.
'''

# import your 2 files here!
from space_map import *
from ship import *

def main():
    '''
    Runs the entire program from start to end. 
    
    All program logic must be executed within the main() function. We have
    provided some starting implementation and comments to help you out.
    '''
    print('>>> STARTING ROUTE: Kepler-452b -> Sector 9-Delta')

    # 1. Configuring navigation systems
    print('\n>> CONFIGURING NAVIGATIONAL SYSTEMS')
    # - Ask for size of map
    while True:
        map_size = int(input('Enter size of map (n >= 2): '))
        if map_size < 2:
            print('Error: n too low')
        # - Then use this size to create a map reusing functions from the space_map 
        else:
            main_map = create_map(map_size)
            print(f'{map_size} x {map_size} map initialised.\n')
            populate_map(main_map)
            break


    # 2. Configuring ship systems
    print('>> NAVIGATIONAL SYSTEMS READY')
    print('\n>> CONFIGURING SHIP SYSTEMS')
    # - Ask for name and fuel of ship
    ship_name = input("Enter ship name: ")
    while True:       
        fuel_amount = int(input("Enter fuel (1-99): "))
        if fuel_amount < 1:
            print("Error: fuel too low")
        elif fuel_amount > 99:
            print("Error: fuel too high")
        else:
        # - Then using the name and fuel, create a Ship instance reusing the Ship
            ship = Ship(ship_name, fuel_amount)
            print(ship)
            print('>> SHIP SYSTEMS READY')
            break

    print('\n>>> EXECUTING LIFTOFF: EXITING Kepler-452b\'s ORBIT')

    print('\n>>> AWAITING COMMANDS\n')
    while True:
        command = input("Enter (n,e,s,w | map | status): ").strip().lower()
        if command not in ('n','e','s','w','map','status', 'q'):
            print("Error: unrecognised command")
        else:
            if command == "map":
                display_map(main_map)
            elif command == "status":
                print(ship)
            elif command == "q":
                print(f"{ship_name} has self-destructed.")
                main_map[ship.y][ship.x] = 'L'
                display_map(main_map)
                print("\n>>> MISSION FAILED")
                break
            elif command in ('n','e','s','w'): 
                new_x = ship.x
                new_y = ship.y   
                
                if command == 's':
                    new_y += 1
                if command == 'n':
                    new_y -= 1
                if command == 'e':
                    new_x += 1
                if command == 'w':
                    new_x -= 1
                if not (0 <= new_x < map_size and 0 <= new_y < map_size):
                        print("Error: out of bounds")
                else:
                    main_map[ship.y][ship.x] = ' '
                    symbol = main_map[new_y][new_x]
                    interaction = ship.interact(symbol, new_x, new_y)
                    if interaction:
                        main_map[new_y][new_x] = '@'
                    else:
                        main_map[ship.y][ship.x] = '@'
                    
                    if ship.destination_reached:
                        main_map[ship.y][ship.x] = 'W'
                        display_map(main_map)
                        print("\n>>> MISSION COMPLETED")
                        break   
                    if ship.is_out_of_fuel():
                        print(f"{ship_name} is out of fuel.")
                        main_map[ship.y][ship.x] = 'L'
                        display_map(main_map)
                        print("\n>>> MISSION FAILED")
                        break
                    if ship.is_out_of_health():
                        main_map[ship.y][ship.x] = 'L'
                        display_map(main_map)
                        print("\n>>> MISSION FAILED")
                        break
                 
                    
                    
                    

                    
                    



                    
                
            

        

    # 3. Game Loop
    # - At this stage, you should have both a map and ship initialised
    # - Take in commands from user to navigate map and progress the game
    # - You'll need to make frequent use of both your map and ship!
    #    - Your ship stores (x, y): This is [y][x] on the map!
    #    - When you find where the ship wants to move, call its interact()
    #      method!
    # - After each interaction, you'll need to check win/loss conditions
    #    - Check if ship reached destination (remember ship stores this!)
    #    - Check if ship has no health
    #    - Check if ship has no fuel left
    # ...


# don't modify this!
if __name__ == '__main__':
    main()
