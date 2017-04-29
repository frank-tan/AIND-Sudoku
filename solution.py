assignments = []

rows = 'ABCDEFGHI'
cols = '123456789'

def cross(A, B):
    "Cross product of elements in A and elements in B."
    return [s + t for s in A for t in B]

boxes = cross(rows, cols)
row_units = [cross(r, cols) for r in rows]
column_units = [cross(rows, c) for c in cols]
square_units = [cross(rs, cs) for rs in ('ABC','DEF','GHI') for cs in ('123','456','789')]
unit_list = row_units + column_units + square_units

def assign_value(values, box, value):
    """
    Please use this function to update your values dictionary!
    Assigns a value to a given box. If it updates the board record it.
    """

    # Don't waste memory appending actions that don't actually change any values
    if values[box] == value:
        return values

    values[box] = value
    if len(value) == 1:
        assignments.append(values.copy())
    return values

def naked_twins(values):
    """Eliminate values using the naked twins strategy.
    Args:
        values(dict): a dictionary of the form {'box_name': '123456789', ...}

    Returns:
        the values dictionary with the naked twins eliminated from peers.
    """

    # Find all instances of naked twins
    # for each unit (row, column or square)
    for unit in unit_list:
        # use a set to track the naked twin we have eliminated for this unit, so we don't eliminate the same twin twice
        naked_twin_set = set()
        # for each box in that unit
        for box_key in unit:
            box_value = values[box_key]
            # if the box has two possible values, find the other box in this unit which has identical values and
            # not eliminated in this unit before
            if len(box_value) == 2:
                naked_twins_keys = [keys for keys in unit if keys not in naked_twin_set and values[keys] == box_value]
                # if there are two boxes in this unit which has identical two possible values
                if len(naked_twins_keys) == 2:
                    # it means we have found a naked twin
                    naked_twin_set.add(naked_twins_keys[0])
                    naked_twin_set.add(naked_twins_keys[1])
                    naked_twin_value_1 = values[naked_twins_keys[0]][0]
                    naked_twin_value_2 = values[naked_twins_keys[0]][1]
                    # Eliminate the naked twins as possibilities for their peers
                    for peer_key in unit:
                        if peer_key not in naked_twins_keys:
                            values[peer_key] = values[peer_key].replace(naked_twin_value_1, '')
                            values[peer_key] = values[peer_key].replace(naked_twin_value_2, '')

    return values

def grid_values(grid):
    """
    Convert grid into a dict of {square: char} with '123456789' for empties.
    Args:
        grid(string) - A grid in string form.
    Returns:
        A grid in dictionary form
            Keys: The boxes, e.g., 'A1'
            Values: The value in each box, e.g., '8'. If the box has no value, then the value will be '123456789'.
    """
    pass

def display(values):
    """
    Display the values as a 2-D grid.
    Args:
        values(dict): The sudoku in dictionary form
    """
    width = 1 + max(len(values[s]) for s in boxes)
    line = '+'.join(['-' * (width * 3)] * 3)
    for r in rows:
        print(''.join(values[r + c].center(width) + ('|' if c in '36' else '')
                      for c in cols))
        if r in 'CF': print(line)
    return

def eliminate(values):
    pass

def only_choice(values):
    pass

def reduce_puzzle(values):
    pass

def search(values):
    pass

def solve(grid):
    """
    Find the solution to a Sudoku grid.
    Args:
        grid(string): a string representing a sudoku grid.
            Example: '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    Returns:
        The dictionary representation of the final sudoku grid. False if no solution exists.
    """

if __name__ == '__main__':
    diag_sudoku_grid = '2.............62....1....7...6..8...3...9...7...6..4...4....8....52.............3'
    display(solve(diag_sudoku_grid))

    try:
        from visualize import visualize_assignments
        visualize_assignments(assignments)

    except SystemExit:
        pass
    except:
        print('We could not visualize your board due to a pygame issue. Not a problem! It is not a requirement.')
