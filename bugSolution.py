def function_with_uncommon_error_solution(x):
    if x == 0:
        return float('inf') # Return infinity instead of raising an error 
    else:
        return x + 5