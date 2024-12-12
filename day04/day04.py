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

def find_horizontal_pattern_count(data, pattern=PATTERN):
    forward_count = 0
    reverse_count = 0
    total = 0
    for line in data:
        # Use re.findall to extract all matches
        forward_count = len(re.findall(pattern, line))
        reverse_count = len(re.findall(pattern[::-1], line))
        total += forward_count+ reverse_count
    return total

def find_vertical_pattern_count(data, pattern=PATTERN):
    total = 0
    puzzle_height = len(data)
    for row in range(puzzle_height):
        col = ""
        for line in data:
            col += line[row]
        total += len(re.findall(pattern, col))
        total += len(re.findall(pattern[::-1], col))
    return total


def find_fwd_diag_fwd_ptrn_cnt(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_height = len(data)
    row_width = len(data[r_idx])
    total = 0
    try:
        if data[r_idx][c_idx] == pattern[0] and \
            (r_idx + len(pattern)) <= puzzle_height and \
            (c_idx - len(pattern)) <= row_width:
            for p_idx in range(len(pattern)):
                if data[r_idx+p_idx][c_idx-p_idx] != pattern[p_idx]:
                    return total
            total += 1
            print("Found pattern at ({},{})".format(r_idx, c_idx))
    except:
        pass
    return total

def find_fwd_diag_bkwd_ptrn_cnt(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_height = len(data)
    row_width = len(data[r_idx])
    total = 0
    try:
        if data[r_idx][c_idx] == pattern[-1] and \
            (r_idx + len(pattern)) <= puzzle_height and \
            (c_idx - len(pattern)) <= row_width:
            for p_idx in range(len(pattern)):
                if data[r_idx+p_idx][c_idx-p_idx] != pattern[len(pattern)-p_idx]:
                    return total
            total += 1
    except:
        pass
    return total

def find_bkwd_diag_fwd_ptrn_cnt(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_height = len(data)
    row_width = len(data[r_idx])
    total = 0
    try:
        if data[r_idx][c_idx] == pattern[0] and \
            (r_idx + len(pattern)) <= puzzle_height and \
            (c_idx + len(pattern)) <= row_width:
            for p_idx in range(len(pattern)):
                if data[r_idx+p_idx][c_idx+p_idx] != pattern[p_idx]:
                    return total
            total += 1
    except:
        pass
    return total

def find_bkwd_diag_bkwd_ptrn_cnt(data, r_idx, c_idx, pattern=PATTERN):
    puzzle_height = len(data)
    row_width = len(data[r_idx])
    total = 0
    try:
        if data[r_idx][c_idx] == pattern[-1] and \
            (r_idx + len(pattern)) <= puzzle_height and \
            (c_idx + len(pattern)) <= row_width:
            for p_idx in range(len(pattern)):
                if data[r_idx+p_idx][c_idx+p_idx] != pattern[len(pattern)-p_idx]:
                    return total
            total += 1
    except:
        pass
    return total

def find_diag_pattern_count(data, pattern=PATTERN):
    '''
    Adjust data for forward diagonal
    For each row, remove the first character, 
    then add a peiod at the end.
    '''
    puzzle_height = len(data)
    total = 0

    # For each row, find the first or last character of PATTERN
    for r_idx in range(puzzle_height):
        row_width = len(data[r_idx])
        for c_idx in range(row_width):
            # Find 
            total += find_fwd_diag_fwd_ptrn_cnt(data, r_idx, c_idx, pattern)
            total += find_fwd_diag_bkwd_ptrn_cnt(data, r_idx, c_idx, pattern)
            total += find_bkwd_diag_fwd_ptrn_cnt(data, r_idx, c_idx, pattern)
            total += find_bkwd_diag_bkwd_ptrn_cnt(data, r_idx, c_idx, pattern)

    return total


def solve(data):
    '''
    Count the number of safe reports.
    '''
    total=0
    total += find_horizontal_pattern_count(data)
    total += find_vertical_pattern_count(data)
    total += find_diag_pattern_count(data)
    # total += find_fwd_diag_pattern_count(data)
    # total += find_bkwd_diag_pattern_count(data)
    return total

def __main__():
    data = get_data()
    print(solve(data)) 

if __name__ == "__main__":
    __main__()