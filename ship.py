'''
ship.py — Ship Module

This module defines the Ship class used in the space exploration game.

The Ship class encapsulates all functionality related to the player's ship,
including the ship's current state (position, fuel, health, and minerals)
and methods to manage movement, resource consumption, interactions with map
entities and displaying status reports.
'''


class Ship:
    def __init__(self, name: str, fuel: int):
        '''
        Initialises a Ship instance with the given name and starting fuel.

        The ship will also begin with some extra attributes set to the 
        following default values:
            x (int): 0
            y (int): 0
            health (int): 3 (full health)
            minerals (int): 0
            destination_reached (bool): False
        '''
        self.name = name
        self.fuel = fuel
        self.x = 0  
        self.y = 0
        self.health = 3
        self.minerals = 0
        self.destination_reached = False


    def consume_fuel(self):
        '''Decreases the ship's fuel by 1 unit, where it can't fall below 0.'''
        if self.fuel > 0:
            self.fuel -= 1
            return self.fuel
        else:
            return None
                       


    def is_out_of_fuel(self) -> bool:
        '''
        Returns True if the ship has no fuel remaining (reaches 0), False
        otherwise.
        '''
        if self.fuel == 0:
            return True
        else:
            return False
        

    def damage_ship(self):
        '''Decreases the ship's health by 1, where it can't fall below 0.'''
        if self.health > 0:
            self.health -= 1
            return self.health
        else:
            return None


    def repair_ship(self):
        '''Increases the ship's health by 1, up to a maximum of 3.'''
        if self.health < 3:
            self.health += 1
            return self.health
        else:
            return None


    def is_out_of_health(self) -> bool:
        '''
        Returns True if the ship has no health remaining (reaches 0), False
        otherwise.
        '''
        if self.health == 0:
            return True
        else:
            return False


    def add_mineral(self):
        '''Increases the ship's minerals by 1. '''
        self.minerals += 1
        return self.minerals


    def use_mineral(self):
        '''Decreases the ship's minerals by 1, where it can't fall below 0.'''
        if self.minerals > 0:
            self.minerals -= 1
            return self.minerals
        else:
            return None


    def land_at_destination(self):
        '''
        Marks that the ship has reached its destination by setting 
        destination_reached to True.
        '''
        self.destination_reached = True
        return self.destination_reached

        
    def interact(self, symbol: str, symbol_x: int, symbol_y: int) -> bool:
        '''
        Handles the ship's interaction with a map entity based on its symbol 
        and coordinates.

        The interaction varies depending on the type of entity. Each 
        interaction may affect the ship's state (e.g., coordinates, health, 
        minerals, etc).

        Parameters:
            symbol (str): The symbol representing the entity 
                    (' ', 'X', '.', 'E', 'M', 'R')
            symbol_x (int): The x-coordinate of the entity
            symbol_y (int): The y-coordinate of the entity
  
        Returns:
            bool: True if the ship moves to the entity's coordinates, 
                  False otherwise.
        '''
        if symbol == ' ':
            self.x = symbol_x
            self.y = symbol_y
            self.fuel -= 1
            return True
        elif symbol == 'X':
            self.x = symbol_x
            self.y = symbol_y
            self.fuel -= 1
            self.destination_reached = True
            print(f'{self.name} has reached: Sector 9-Delta')
            return True
        elif symbol == '.':
            print(f'Cannot move past an asteroid!')
            return False
        elif symbol == 'E':
            self.x = symbol_x
            self.y = symbol_y           
            self.fuel -= 1
            self.health -= 1
            if self.health <= 0: 
                print(f'{self.name} has fallen.')
                return True
            else:
                print(f'We won the fight! Health: {self.health}/3')
                return True
        elif symbol == 'M':
            self.x = symbol_x
            self.y = symbol_y           
            self.fuel -= 1
            self.minerals += 1
            print (f'+1 mineral! Minerals: {self.minerals}')
            return True
        elif symbol == "R":
            if self.health == 3:
                print(f'Ship is already at full health!')
                return False
            elif 0 < self.health < 3 and self.minerals == 0:
                print(f'You need a mineral to activate this repair station.')
                return False
            else:
                self.x = symbol_x
                self.y = symbol_y
                self.fuel -= 1
                self.minerals -= 1
                self.health += 1
                print(f'Ship repaired! Health: {self.health}/3')
                return True


    def __str__(self) -> str:
        '''Returns a status report summarising the ship's current state.'''
        line = '-' * 25
        status = f'''Status Report - {self.name}
{line}
Coordinates    : ({self.x}, {self.y})
Fuel Level     : {self.fuel:02} units
Health         : {self.health}
Minerals       : {self.minerals:02}
{line}'''
        return status


if __name__ == '__main__':
    # you can put any test code here!
    # this only runs when its the main program ran i.e. python3 ship.py
    pass
