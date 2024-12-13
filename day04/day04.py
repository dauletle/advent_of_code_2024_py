import os
import re

PATTERN = 'XMAS'

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

def find_horizontal_pattern_count(data, c_idx, r_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    if r_idx+len(PATTERN)>puzzle_height:
        # Horizontal
        pattern_found = True
        for p_idx, p_char in enumerate(PATTERN):
            if data[r_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
        # Horizontal reversed
        pattern_found = True
        for p_idx, p_char in enumerate(reversed(PATTERN)):
            if data[r_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
    return total

def find_vertical_pattern_count(data, c_idx, r_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    if r_idx+len(PATTERN)>puzzle_height:
        # Vertical
        pattern_found = True
        for p_idx, p_char in enumerate(PATTERN):
            if data[r_idx+p_idx][c_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
        # Vertical reversed
        pattern_found = True
        for p_idx, p_char in enumerate(reversed(PATTERN)):
            if data[r_idx+p_idx][c_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
    return total

def find_bkwd_diag_pattern_count(data, r_idx, c_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    if r_idx-len(PATTERN)>0 and c_idx+len(PATTERN)<puzzle_width:
        # Backward diagonal
        pattern_found = True
        for p_idx, p_char in enumerate(PATTERN):
            if data[r_idx-len(PATTERN)][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
        # Backward diagonal reversed
        pattern_found = True
        for p_idx, p_char in enumerate(reversed(PATTERN)):
            if data[r_idx-len(PATTERN)][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
    return total

def find_fwd_diag_pattern_count(data, r_idx, c_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    if r_idx+len(PATTERN)>0 and c_idx+len(PATTERN)<puzzle_width:
        # Forward diagonal
        pattern_found = True
        for p_idx, p_char in enumerate(PATTERN):
            if data[r_idx+p_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
        # Forward diagonal reversed
        pattern_found = True
        for p_idx, p_char in enumerate(reversed(PATTERN)):
            if data[r_idx+p_idx][c_idx+p_idx] != p_char:
                pattern_found = False
                break
        if pattern_found:
            total += 1
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
            total += find_horizontal_pattern_count(data, c_idx, r_idx)
            total += find_vertical_pattern_count(data, c_idx, r_idx)
            total += find_fwd_diag_pattern_count(data, r_idx, c_idx)
            total += find_bkwd_diag_pattern_count(data, r_idx, c_idx)

    return total

def __main__():
    data = get_data()
    print(solve(data)) 

if __name__ == "__main__":
    __main__()