import random

def generate_units(num_units, max_weight, max_value):
    units = []
    for _ in range(num_units):
        weight = random.randint(1, max_weight)
        value = random.randint(1, max_value)
        units.append((weight, value))
    return units

## Task 2.1
# Recursive function used to build dynamic programming function
def knapsack_01(units, n, max_capacity):
    if n == 0 or max_capacity == 0:
        return 0, 0

    #Current item
    weight, value = units[n-1]

    #If Item is to heavy, skip it and move on to next item (n-1)
    if weight > max_capacity:
        return knapsack_01(units, n-1, max_capacity)

    #Item should be included
    val_with_item, weight_with_item = knapsack_01(units, n-1, max_capacity-weight)

    #Item should not be included
    val_without_item, weight_without_item = knapsack_01(units, n-1, max_capacity)

    #Compare value of knapsack when current item is included and when it is not included
    #If value of knapsack is more when item is included, include the item
    if value + val_with_item > val_without_item:
        print("Item included: ", units[n-1])
        return value + val_with_item, weight + weight_with_item
    else:
        print("Item not included: because ", value + val_with_item, " < ", val_without_item)
        return val_without_item, weight_without_item

#Dynamic programming of knapsack problem
def knapsack_01_dp(units, max_capacity):
    #Number of units
    n = len(units)

    #Create a table to store results of subproblems
    dp_table = []
    for i in range(n + 1):
        dp_table.append([])
        for j in range(max_capacity + 1):
            dp_table[i].append(0)

    # Build dp_table
    for i in range(1, n+1):
        for w in range(1, max_capacity+1):
            # current item
            current_weight, current_value = units[i-1]

            # If weight of current item is more than capacity of knapsack, then this item is not included
            # And we take the value from the previous item at that capacity
            if current_weight > w:
               dp_table[i][w] = dp_table[i-1][w]
            else:

                value_with_item = current_value + dp_table[i-1][w-current_weight]
                value_without_item = dp_table[i-1][w]

                # The cell is filled with the maximum of these two values
                dp_table[i][w] = max(value_with_item, value_without_item)

    # After filling the dp_table, the maximum value of knapsack is at the bottom right corner
    # of the table that can be achieved using the given parameters
    for row in dp_table:
        print(' '.join(map(str, row)))
    return dp_table[n][max_capacity]

# Greedy programming of knapsack problem, recursive
def knapsack_fractional(units, max_capacity, index=0):
    if index >= len(units) or max_capacity <= 0:
        return 0, 0

    #Current item
    weight, value = units[index]

    #If weight of item is less than or equal to max capacity of knapsack, include the item
    if weight <= max_capacity:
        print("FR ---- Item included: ", units[index])
        total_value, total_weight = knapsack_fractional(units, max_capacity - weight, index + 1)
        return round(value + total_value, 2), weight + total_weight
    #If weight of item is more than max capacity of knapsack, include fraction of item
    else:
        fraction = max_capacity / weight
        print("#### //// #### Fraction included: ", units[index], "Fraction: ", fraction)
        return round(value * fraction, 2), max_capacity


# Example usage
num_units = 5
max_weight = 60
max_value = 300
max_capacity = 70

# Generate random units
units = generate_units(num_units, max_weight, max_value)

# Solve 0-1 and fractional knapsack problems
# solution_01 = knapsack_01(units, len(units), max_capacity)
solution_fractional = knapsack_fractional(units, max_capacity)

dp_solution = knapsack_01_dp(units, max_capacity)

print("units:", units)
# print(f"0-1 Knapsack Solution: VALUE {solution_01[0]}, WEIGHT: {solution_01[1]}")
print(f"DP Knapsack Solution: {dp_solution}")
print(f"Fractional Knapsack Solution: VALUE {solution_fractional[0]}, WEIGHT: {solution_fractional[1]}")
