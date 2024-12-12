import os
import re

def get_data():
    '''
    Get data from file
    '''
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = ''
    with open(input_filename, "r") as f:
        # Read data
        data = f.read()
    return data

def extract_mul_expressions(data):
    '''
    Extract all mul expressions from data. 
    "mul(X,Y)", where X and Y are each 1-3 digit numbers.
    '''
    # Define the regex pattern
    pattern = r"mul\(\d{1,3},\d{1,3}\)"
    # Use re.findall to extract all matches
    matches = re.findall(pattern, data)
    return matches

def execute_mul_expression(expression):
    # Regular expression pattern to extract numbers
    pattern = r"mul\((\d+),(\d+)\)"
    match = re.match(pattern, expression)
    if match:
        # Extract the captured groups
        x, y = match.groups()
        return int(x) * int(y)

def solve(data):
    '''
    Count the number of safe reports.
    '''
    total=0
    extracted_numbers = extract_mul_expressions(data)
    for expression in extracted_numbers:
        total += execute_mul_expression(expression)
    return total

def __main__():
    data = get_data()
    print(solve(data)) 

if __name__ == "__main__":
    __main__()