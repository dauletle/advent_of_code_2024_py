import os
from collections import namedtuple

MapCoordinateInfo = namedtuple('MapCoordinateInfo', 'obstructed visited')
guard_chars = ['^', '>', 'v', '<']

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

def get_map_info(input_data):
    data = []
    # For each line in f, for each character in line, append to data
    for line in input_data:
        data_line = []
        for char in line:
            data_line.append(MapCoordinateInfo(char == '#', char in guard_chars))
        data.append(data_line)

def solve(data):
    map = get_map_info(data)
    print(map)

def __main__():
    data = get_data()
    solve(data)

if __name__ == "__main__":
    __main__()