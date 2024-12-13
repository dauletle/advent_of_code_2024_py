import os

class MapCoordinateInfo:
    def __init__(self, obstructed, visited):
        self.obstructed = obstructed
        self.visited = visited

guard_directions = {
        '^': (0, -1),
        '>': (1, 0),
        'v': (0, 1),
        '<': (-1, 0)
    }

def get_data():
    '''
    Get data from file
    '''
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        # Read data, split by newline
        data = f.read().split("\n")
    return data

class Guard:
    def __init__(self, coordinate, direction):
        self.coordinate = coordinate
        self.direction = direction
        self.in_room = True
    
    def are_coordinates_in_room(self, map, coordinate):
        map_height = len(map)
        map_width = len(map[0])
        if coordinate[0] == map_width or coordinate[0] < 0:
            return False
        elif coordinate[1] == map_height or coordinate[1] < 0:
            return False
        return True

    def move(self, map):
        next_coordinate = (
            self.coordinate[0] + guard_directions[self.direction][0],
            self.coordinate[1] + guard_directions[self.direction][1]
        )
        if self.are_coordinates_in_room(map, next_coordinate) and \
                map[next_coordinate[0]][next_coordinate[1]].obstructed:
            directions = list(guard_directions.keys())
            next_direction_index = (directions.index(self.direction) + 1) % 4
            self.direction = directions[next_direction_index]
            
        self.coordinate = (
            self.coordinate[0] + guard_directions[self.direction][0],
            self.coordinate[1] + guard_directions[self.direction][1]
        )

class MapSimulator:
    def __init__(self, input_data):
        self.guards = []
        self.positions_visited = 0
        self.map = self.get_map_info(input_data)
        self.map_height = len(self.map)
        self.map_width = len(self.map[0])
        self.run_guards()

    def get_map_info(self, input_data):
        # Initialize the data structure with empty lists for each x_index
        data = [[] for _ in range(len(input_data[0]))]
        
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
        if guard.coordinate[0] == self.map_width or guard.coordinate[0] < 0:
            guard.in_room = False
        elif guard.coordinate[1] == self.map_height or guard.coordinate[1] < 0:
            guard.in_room = False

    def are_all_guards_in_room(self):
        for guard in self.guards:
            if guard.in_room:
                return True
        return False
    
    def run_guards(self):
        while self.are_all_guards_in_room():
            for guard in self.guards:
                guard.move(self.map)
                self.update_if_guard_in_room(guard)
                if guard.in_room:
                    cell = self.map[guard.coordinate[0]][guard.coordinate[1]]
                    if not cell.visited:
                        cell.visited = True
                        self.map[guard.coordinate[0]][guard.coordinate[1]] = cell
                        self.positions_visited += 1



def __main__():
    data = get_data()
    sim = MapSimulator(data)
    print("Number of positions visited by guards:", sim.positions_visited)

if __name__ == "__main__":
    __main__()