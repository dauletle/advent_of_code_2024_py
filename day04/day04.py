import os
import re

PATTERN = 'XMAS'
DEBUG = False

def get_data():
    '''
    Get data from file
    '''
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = ''
    with open(input_filename, "r") as f:
        # Read data
        data = f.read().split("\n")
    return data

def find_horizontal_pattern_count(data, c_idx, r_idx, pattern=PATTERN):
    puzzle_height = len(data)
    total = 0
    list_of_coordinates = []
    if c_idx+len(pattern)<=puzzle_height:
        # Horizontal
        pattern_found = True
        for p_idx, p_char in enumerate(pattern):
            if data[r_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
            else:
                list_of_coordinates.append((r_idx, c_idx+p_idx))
        if pattern_found:
            total += 1
            if DEBUG: print("Horizontal pattern found at: ", list_of_coordinates)
    return total

def find_vertical_pattern_count(data, c_idx, r_idx, pattern=PATTERN):
    puzzle_height = len(data)
    total = 0
    list_of_coordinates = []
    if r_idx+len(pattern)<=puzzle_height:
        # Vertical
        pattern_found = True
        for p_idx, p_char in enumerate(pattern):
            if data[r_idx+p_idx][c_idx] != p_char:
                pattern_found = False
                break
            else:
                list_of_coordinates.append((r_idx+p_idx, c_idx))
        if pattern_found:
            total += 1
            if DEBUG: print("Vertical pattern found at: ", list_of_coordinates)
    return total

def find_bkwd_diag_pattern_count(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_width = len(data[0])
    total = 0
    list_of_coordinates = []
    if r_idx-len(pattern)>=0 and c_idx+len(pattern)<=puzzle_width:
        # Backward diagonal
        pattern_found = True
        for p_idx, p_char in enumerate(pattern):
            if data[r_idx-p_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
            else:
                list_of_coordinates.append((r_idx-p_idx, c_idx+p_idx))
        if pattern_found:
            total += 1
            if DEBUG: print("Forward diagonal pattern found at: ", list_of_coordinates)
    return total

def find_fwd_diag_pattern_count(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_width = len(data[0])
    total = 0
    list_of_coordinates = []
    if r_idx+len(pattern)<=puzzle_width and c_idx+len(pattern)<=puzzle_width:
        # Forward diagonal
        pattern_found = True
        for p_idx, p_char in enumerate(pattern):
            if data[r_idx+p_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
            else:
                list_of_coordinates.append((r_idx+p_idx, c_idx+p_idx))
        if pattern_found:
            total += 1
            if DEBUG: print("Reverse diagonal pattern found at: ", list_of_coordinates)
    return total


def solve(data):
    '''
    Count the number of safe reports.
    '''
    puzzle_height = len(data)
    total = 0
    for r_idx in range(puzzle_height):
        row_width = len(data[r_idx])
        for c_idx in range(row_width):
            # Check pattern and reverse pattern.
            for pattern in [PATTERN, PATTERN[::-1]]:
                total += find_horizontal_pattern_count(data, c_idx, r_idx, pattern)
                total += find_vertical_pattern_count(data, c_idx, r_idx, pattern)
                total += find_fwd_diag_pattern_count(data, r_idx, c_idx, pattern)
                total += find_bkwd_diag_pattern_count(data, r_idx, c_idx, pattern)

    return total

def __main__():
    data = get_data()
    print(solve(data)) 

if __name__ == "__main__":
    __main__()