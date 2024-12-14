import os

def get_data():
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = []
    with open(input_filename, "r") as f:
        # Read data, split by newline
        data = f.read().split("\n")
    return data

def is_target_value_valid(target_value, terms):
    if len(terms) == 1:
        return terms[0] == target_value
    # Use recursion to find the target value is valid using summation.
    if is_target_value_valid(target_value, [terms[0] + terms[1]] + terms[2:]):
        return True
    # Use recursion to find the target value is valid using multiplication.
    if is_target_value_valid(target_value, [terms[0] * terms[1]] + terms[2:]):
        return True
    return False

def covert_to_expression(line):
    value, expression = line.split(": ")
    target_value = int(value)
    terms = [int(x) for x in expression.split(" ")]
    return target_value, terms

def __main__():
    data = get_data()
    total_cal_result = 0
    for line in data:
        target_value, terms = covert_to_expression(line)
        if is_target_value_valid(target_value, terms):
            total_cal_result += target_value
        print()
    print("Total Calibration Result:", total_cal_result)
    

if __name__ == "__main__":
    __main__()