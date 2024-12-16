import os

class Antenna:
    def __init__(self, antennaType, coordinates):
        self.antennaType = antennaType
        self.coordinates = [coordinates]
        self.unique_pairs = list()
        self.antinode = list()
        self.total_antinode = 0

    def get_coordinates(self):
        return self.coordinates
    
    def add_coordinates(self, coordinates):
        self.coordinates.append(coordinates)
    
    def get_unique_pairs(self):
        return self.unique_pairs
    
    def add_unique_pair(self, pair):
        if pair in self.unique_pairs:
            return
        self.unique_pairs.append(pair)


class AntennaMap:
    def __init__(self, input_data):
        self.map_height = len(input_data)
        self.map_width = len(input_data[0])
        self.antennas = dict()
    
    def collect_antennas(self, input_data):
        for r_idx, line in enumerate(input_data):
            for c_idx, char in enumerate(line):
                if char != '.':
                    if char not in self.antennas.keys():
                        self.antennas[char] = Antenna(char, (c_idx, r_idx))
                    else:
                        self.antennas[char].add_coordinates((c_idx, r_idx))
    
    def get_antenna_unique_pairs(self, antenna):
        coordinates = self.antennas[antenna].get_coordinates()
        for i in range(len(coordinates)):
            for j in range(i + 1, len(coordinates)):
                self.antennas[antenna].add_unique_pair([coordinates[i], coordinates[j]])
    
    def check_coordinates(self, coordinate):
        if coordinate[0] >= self.map_width or coordinate[0] < 0:
            return False
        elif coordinate[1] >= self.map_height or coordinate[1] < 0:
            return False
        return True
    
    def determine_antinode(self, antenna, pair):
        pair_spread = [pair[0][0] - pair[1][0], pair[0][1] - pair[1][1]]
        antinode_1 = [pair[0][0] + pair_spread[0], pair[0][1] + pair_spread[1]]
        antinode_2 = [pair[1][0] - pair_spread[0], pair[1][1] - pair_spread[1]]
        if self.check_coordinates(antinode_1):
            self.antennas[antenna].antinode.append(antinode_1)
        if self.check_coordinates(antinode_2):
            self.antennas[antenna].antinode.append(antinode_2)
    
    def calculate_total_antinode(self):
        list_of_antinode = list()
        for antenna in self.antennas.keys():
            for antinode in self.antennas[antenna].antinode:
                if antinode not in list_of_antinode:
                    list_of_antinode.append(antinode)
        return len(list_of_antinode)

        

def get_data():
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        # Read data, split by newline
        data = f.read().split("\n")
    return data



def __main__():
    data = get_data()
    am = AntennaMap(data)
    am.collect_antennas(data)
    for antenna in am.antennas.keys():
        am.get_antenna_unique_pairs(antenna)
        for pair in am.antennas[antenna].get_unique_pairs():
            am.determine_antinode(antenna, pair)
    # Print total number of antinodes
    print("Total number of antinode:", am.calculate_total_antinode())
    
    

if __name__ == "__main__":
    __main__()