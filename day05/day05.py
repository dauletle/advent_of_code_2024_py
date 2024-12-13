import os

def get_data():
    '''
    Get data from file
    '''
    current_dir = os.path.dirname(__file__)
    input_filename = os.path.join(current_dir, "input.txt")
    data = ''
    with open(input_filename, "r") as f:
        # Read data, split by double newline
        data = f.read().split("\n\n")
    return data

def get_rules(data):
    rules_section = data[0]
    # For each rule in a line, split the order of pages by '|'
    rules = []
    for rule in rules_section.split("\n"):
        rules.append([int(x) for x in rule.split("|") if x.isdigit()])
    return rules

def get_page_order(data):
    page_order_section = data[1]
    page_order = []
    # For each page order in a line, split the order of pages by ','
    for page in page_order_section.split("\n"):
        page_order.append([int(x) for x in page.split(",") if x.isdigit()])
    return page_order

def list_acceptable_updates(rules, page_order):
    valid_page_orders = []
    page_order_valid = True
    for update in page_order:
        for rule in rules:
            if page_order_valid == False:
                break
            if rule[0] in update and rule[1] in update and \
                  update.index(rule[0]) >= update.index(rule[1]):
                page_order_valid = False
        if page_order_valid:
            valid_page_orders.append(update)
    return valid_page_orders

def get_middle_page(page_order):
    middle_page = len(page_order) // 2
    return page_order[middle_page]

def solve(data):
    rules = get_rules(data)
    page_order = get_page_order(data)
    valid_page_orders = list_acceptable_updates(rules, page_order)
    print("List of acceptable page orders:")
    for page_order in valid_page_orders:
        print("\t", page_order)
    print("Sum of middle pages:", sum([get_middle_page(page_order) for page_order in valid_page_orders]))
    return valid_page_orders

def __main__():
    data = get_data()
    solve(data)

if __name__ == "__main__":
    __main__()