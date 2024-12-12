import os

def get_data():
    '''
    Get data from file, splitting columns by space, and rows by newline.
    '''
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        data = f.read().split("\n")
        data = [line.strip().split() for line in data]
    return data

def report_is_safe(level, next_level, increasing):
    '''
    Check if a report is safe.
    The levels are either all increasing or all decreasing.
    Any two adjacent levels differ by at least one and at most three.
    '''
    adj_level_diff = abs(next_level - level)
    if adj_level_diff < 1 or adj_level_diff > 3: 
        return False
    if increasing and next_level < level: 
        return False
    if not increasing and next_level > level: 
        return False
    return True

def solve(data):
    '''
    Count the number of safe reports.
    '''
    total_safe=0
    # Check each row, and call it safe if all conditions are met
    for report in data:
        safe = True
        increasing = True
        # Check each level in a report
        for idx, level_str in enumerate(report):
            # Define next level, and skip if there is no next level.
            next_level_idx = idx + 1
            if next_level_idx == len(report): 
                continue
            level = int(level_str)
            next_level = int(report[next_level_idx])
            # Define if the report is increasing or decreasing at first level.
            if idx == 0 and level > next_level:
                increasing = False
            # Stop checking rest of levels if the report is not safe.
            if not report_is_safe(level, next_level, increasing):
                safe = False
                break
        if safe: 
            total_safe += 1
    return total_safe

def __main__():
    data = get_data()
    print(solve(data))   

if __name__ == "__main__":
    __main__()