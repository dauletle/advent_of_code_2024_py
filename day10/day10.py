import os
from collections import deque

def get_list_of_input_files():
    current_dir = os.path.dirname(__file__)
    input_filenames = []
    for f in os.listdir(current_dir):
        if f.endswith(".txt") and f.startswith("input"):
            input_filenames.append(os.path.join(current_dir, f))
    return input_filenames

def get_data(input_filename):
    data = []
    with open(input_filename, "r") as f:
        # Read data
        data = f.read().split("\n")
    return data

trail_directions = {
    '^': (0, -1),  # Move up
    '>': (1, 0),   # Move right
    'v': (0, 1),   # Move down
    '<': (-1, 0)   # Move left
}
        

class Map:
    def __init__(self, data):
        self.width = len(data[0])
        self.height = len(data)
        self.max_height = 9
        self.sum_score_trails = 0
        self.trailheads = set()
        # Define trails as a dictionary with key as trailhead position
        self.trails = dict()
        self.map = self.get_map_info(data)
    
    def get_map_info(self, input_data):
        map = []
        for row in input_data:
            map_row = []
            for char in row:
                map_row.append(int(char))
            map.append(map_row)
        return map
    
    def navigate_map(self):
        for row_idx, row in enumerate(self.map):
            for col_idx, height in enumerate(row):
                if self.map[row_idx][col_idx] == 0:
                    self.trailheads.add((row_idx, col_idx))
                    self.sum_score_trails += self.navigate_trails(row_idx, col_idx)

    def navigate_trails(self, x, y):
        coord_height = self.map[x][y]
        if coord_height == self.max_height:
            return 1
        if (x, y) in self.trails:
            return self.trails[(x, y)]
        score = 0
        for direction in trail_directions.keys():
            dx, dy = trail_directions[direction]
            new_x = x + dx
            new_y = y + dy
            if 0 <= new_x < self.width and 0 <= new_y < self.height:
                new_height = self.map[new_x][new_y]
                if new_height == coord_height + 1:
                    score += self.navigate_trails(new_x, new_y)
        self.trails[(x, y)] = score
        return score

    def navigate_trails_bfs(self, x, y):
        trail_queue = deque([(x, y)])
        print("Queue:", trail_queue)
        score = 0
        previously_visited = set()
        while trail_queue:
            x, y = trail_queue.popleft()
            print("Queue:", trail_queue)
            if (x, y) in previously_visited:
                continue
            previously_visited.add((x, y))
            if self.map[x][y] == self.max_height:
                print(f"Full trail found at ({x}, {y}) with height {self.map[x][y]}")
                score += 1
            for direction in trail_directions.keys():
                dx, dy = trail_directions[direction]
                new_x = x + dx
                new_y = y + dy
                if 0 <= new_x < self.width and 0 <= new_y < self.height:
                    new_height = self.map[new_x][new_y]
                    if new_height == self.map[x][y] + 1:
                        # print(f"Found trail from ({x}, {y}) with height {self.map[x][y]} to ({new_x}, {new_y}) with height {new_height}")
                        trail_queue.append((new_x, new_y))
                        print("Queue:", trail_queue)
        return score
    
   

def __main__():
    for input_filename in get_list_of_input_files():
        # Get filename from path input_filename
        filename = os.path.basename(input_filename)
        data = get_data(input_filename)
        map = Map(data)
        print("\n\nNavigating map {}...".format(filename))
        map.navigate_map()
        print(f"Number of trailheads for {filename}: {len(map.trailheads)}")
        print(f"Sum of trail scores for {filename}: {map.sum_score_trails}")
    

if __name__ == "__main__":
    __main__()