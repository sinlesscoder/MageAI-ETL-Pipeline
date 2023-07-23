def add_object(*args) -> dict:
    results =  {}

    for i, arg in enumerate(args):
        results[i] = arg
    
    return results

print(add_object(5, 6, 7, 8, 9, 10))