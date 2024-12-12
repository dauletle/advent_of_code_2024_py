import os

def get_lists():
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    left_column = []
    right_column = []
    with open(input_filename, "r") as f:
        data = f.read().split("\n")
        data = [line.strip().split() for line in data]
        left_column = [int(line[0]) for line in data]
        right_column = [int(line[1]) for line in data]
    return left_column, right_column

def solve(left_column, right_column):
    total=0
    for a, b in zip(sorted(left_column), sorted(right_column)):
        total += abs(a - b)
    return total

def __main__():
    left_column, right_column = get_lists()
    print(solve(left_column, right_column))   

if __name__ == "__main__":
    __main__()