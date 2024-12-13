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
    # Horizontal
    if c_idx+3<puzzle_width and \
            data[r_idx][c_idx]=='X' and \
            data[r_idx][c_idx+1]=='M' and \
            data[r_idx][c_idx+2]=='A' and \
            data[r_idx][c_idx+3]=='S':
        total += 1
    # Horizontal reversed
    if c_idx+3<puzzle_width and \
            data[r_idx][c_idx]=='S' and\
            data[r_idx][c_idx+1]=='A' and \
            data[r_idx][c_idx+2]=='M' and \
            data[r_idx][c_idx+3]=='X':
        total += 1
    return total

def find_vertical_pattern_count(data, c_idx, r_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    # Vertical
    if r_idx+3<puzzle_height and \
            data[r_idx][c_idx]=='X' and \
            data[r_idx+1][c_idx]=='M' and \
            data[r_idx+2][c_idx]=='A' and \
            data[r_idx+3][c_idx]=='S': 
        total += 1
    # Vertical reversed
    if r_idx+3<puzzle_height and \
            data[r_idx][c_idx]=='S' and \
            data[r_idx+1][c_idx]=='A' and \
            data[r_idx+2][c_idx]=='M' and \
            data[r_idx+3][c_idx]=='X':
        total += 1
    return total

def find_bkwd_diag_pattern_count(data, r_idx, c_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    # Backward diagonal
    if r_idx-3>=0 and c_idx+3<puzzle_width and \
                    data[r_idx][c_idx]=='X' and \
                    data[r_idx-1][c_idx+1]=='M' and \
                    data[r_idx-2][c_idx+2]=='A' and \
                    data[r_idx-3][c_idx+3]=='S':
        total += 1
    # Backward diagonal reversed
    if r_idx-3>=0 and c_idx+3<puzzle_width and \
                    data[r_idx][c_idx]=='S' and \
                    data[r_idx-1][c_idx+1]=='A' and \
                    data[r_idx-2][c_idx+2]=='M' and \
                    data[r_idx-3][c_idx+3]=='X':
        total += 1
    return total

def find_fwd_diag_pattern_count(data, r_idx, c_idx):
    puzzle_height = len(data)
    puzzle_width = len(data[0])
    total = 0
    # Forward diagonal
    if r_idx+3<puzzle_height and c_idx+3<puzzle_width and \
            data[r_idx][c_idx]=='X' and \
            data[r_idx+1][c_idx+1]=='M' and \
            data[r_idx+2][c_idx+2]=='A' and \
            data[r_idx+3][c_idx+3]=='S':
        total += 1
    # Forward diagonal reversed
    if r_idx+3<puzzle_height and \
            c_idx+3<puzzle_width and \
            data[r_idx][c_idx]=='S' and \
            data[r_idx+1][c_idx+1]=='A' and \
            data[r_idx+2][c_idx+2]=='M' and \
            data[r_idx+3][c_idx+3]=='X':
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