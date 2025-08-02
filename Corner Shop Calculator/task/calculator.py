def calculate_income(inventory:dict, deductions=0.0) -> float:
    """Return the net income based on the inventory of a fictitious store"""
    income = sum(value['earned'] for value in inventory.values())
    net = income - deductions

    return net

def request_deductions() -> float:
    staff_expenses = float(input('Staff expenses: '))
    other_expenses = float(input('Other expenses: '))

    return staff_expenses + other_expenses

def print_report(report:str, inventory:dict) -> float:
    """Prints a report based on the inventory from a fictitious store"""

    if report == 'price':
        header = 'Prices:'
        footer = ''
    elif report == 'earned':
        header = 'Earned amount:'
        footer = f"\nIncome: ${calculate_income(inventory)}"

    print(header)
    for key, value in inventory.items():
        print(f"{key}: ${value[report]}")
    print(footer)

def main():

    inventory = {'Bubblegum': {'price': 2, 'earned': 202},
              'Toffee': {'price': 0.2, 'earned': 118},
              'Ice cream': {'price': 5, 'earned': 2250},
              'Milk chocolate': {'price': 4, 'earned': 1680},
              'Doughnut': {'price': 2.5, 'earned': 1075},
              'Pancake': {'price': 3.2, 'earned': 80}}

    print_report('earned', inventory)
    deductions = request_deductions()
    print(f"Net income: ${calculate_income(inventory, deductions)}")





if __name__ == '__main__':
    main()
