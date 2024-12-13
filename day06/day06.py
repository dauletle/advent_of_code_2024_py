import os

class MapCoordinateInfo:
    """
    Represents information about a map coordinate.
    
    Attributes:
        obstructed (bool): Whether the coordinate is obstructed.
        visited (bool): Whether the coordinate has been visited by a guard.
    """
    def __init__(self, obstructed, visited):
        self.obstructed = obstructed
        self.visited = visited

guard_directions = {
    '^': (0, -1),  # Move up
    '>': (1, 0),   # Move right
    'v': (0, 1),   # Move down
    '<': (-1, 0)   # Move left
}

def get_data():
    """
    Reads the input data from a file and returns it as a list of strings.

    Returns:
        list: The input data split by newline.
    """
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        # Read data, split by newline
        data = f.read().split("\n")
    return data

class Guard:
    """
    Represents a guard that moves on the map.

    Attributes:
        coordinate (tuple): The (x, y) position of the guard.
        direction (str): The current direction the guard is facing ('^', '>', 'v', '<').
        in_room (bool): Whether the guard is still within the map bounds.
    """
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.direction = direction
        self.in_room = True

    def are_coordinates_in_room(self, map, coordinate):
        """
        Checks if the given coordinate is within the bounds of the map.

        Args:
            map (list): The map data structure.
            coordinate (tuple): The coordinate to check.

        Returns:
            bool: True if the coordinate is within bounds, False otherwise.
        """
        map_height = len(map)
        map_width = len(map[0])
        if coordinate[0] == map_width or coordinate[0] < 0:
            return False
        elif coordinate[1] == map_height or coordinate[1] < 0:
            return False
        return True

    def move(self, map):
        """
        Moves the guard based on its current direction. If the next coordinate
        is obstructed, the guard changes its direction.
        
        Args:
            map (list): The map data structure.
        """
        next_coordinate = (
            self.coordinate[0] + guard_directions[self.direction][0],
            self.coordinate[1] + guard_directions[self.direction][1]
        )
        # Check if the next coordinate is obstructed, and update the direction 
        # if it is obstructed.
        if self.are_coordinates_in_room(map, next_coordinate) and \
                map[next_coordinate[0]][next_coordinate[1]].obstructed:
            # List the available directions
            directions = list(guard_directions.keys())
            # Get the index of the next direction, looping around if necessary.
            next_direction_index = (directions.index(self.direction) + 1) % len(directions)
            # Update the direction
            self.direction = directions[next_direction_index]
        
        # Move the guard in the current direction
        self.coordinate = (
            self.coordinate[0] + guard_directions[self.direction][0],
            self.coordinate[1] + guard_directions[self.direction][1]
        )

class MapSimulator:
    """
    Simulates the movement of guards on a map and tracks visited positions.

    Attributes:
        guards (list): A list of Guard objects.
        positions_visited (int): The number of positions visited by guards.
        map (list): The map data structure.
        map_height (int): The height of the map.
        map_width (int): The width of the map.
    """
    def __init__(self, input_data):
        self.guards = []
        self.positions_visited = 0
        self.map = self.get_map_info(input_data)
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.run_guards()

    def get_map_info(self, input_data):
        """
        Parses the input data to create the map structure and initializes guards.

        Args:
            input_data (list): The input data containing the map layout.

        Returns:
            list: The parsed map data structure.
        """
        # Initialize the data structure with empty lists for each x_index
        data = [[] for _ in range(len(input_data[0]))]
        
        # Parse each line and character to populate the map and guards
        for r_idx, line in enumerate(input_data):
            for c_idx, char in enumerate(line):
                obstructed = char == '#'
                visited = char in guard_directions.keys()
                # Append to the corresponding x_index (column) list
                data[c_idx].append(MapCoordinateInfo(obstructed, visited))
                if char in guard_directions.keys():
                    new_guard = Guard(coordinate=(c_idx, r_idx), direction=char)
                    self.guards.append(new_guard)
                    self.positions_visited += 1
        return data
    
    def update_if_guard_in_room(self, guard):
        """
        Updates the in_room status of a guard based on its current position.

        Args:
            guard (Guard): The guard to update.
        """
        if guard.coordinate[0] == self.map_width or guard.coordinate[0] < 0:
            guard.in_room = False
        elif guard.coordinate[1] == self.map_height or guard.coordinate[1] < 0:
            guard.in_room = False

    def are_all_guards_in_room(self):
        """
        Checks if any guards are still within the map bounds.

        Returns:
            bool: True if at least one guard is in the room, False otherwise.
        """
        # Check each guard's in_room status
        for guard in self.guards:
            if guard.in_room:
                return True
        return False
    
    def run_guards(self):
        """
        Executes the simulation of guards moving on the map until all guards
        are out of bounds.
        """
        while self.are_all_guards_in_room():
            # Move each guard and update visited positions
            for guard in self.guards:
                guard.move(self.map)
                self.update_if_guard_in_room(guard)
                if guard.in_room:
                    cell = self.map[guard.coordinate[0]][guard.coordinate[1]]
                    # Update the cell if it hasn't been visited
                    if not cell.visited:
                        cell.visited = True
                        self.map[guard.coordinate[0]][guard.coordinate[1]] = cell
                        self.positions_visited += 1

def __main__():
    """
    Main function to load the input data and run the simulation.
    """
    data = get_data()
    sim = MapSimulator(data)
    print("Number of positions visited by guards:", sim.positions_visited)

if __name__ == "__main__":
    __main__()