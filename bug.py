def function_with_uncommon_error(x):
    if x == 0:
        return 1 / x  # ZeroDivisionError, but it's caught
    elif x < 0:
        raise ValueError("x must be non-negative")
    else:
        return x + 1

# Example usage
try:
    result = function_with_uncommon_error(-1)
    print(f"Result: {result}")
except ValueError as e:
    print(f"Caught ValueError: {e}")

try:
    result = function_with_uncommon_error(0)
    print(f"Result: {result}")
except ZeroDivisionError as e:
    print(f"Caught ZeroDivisionError: {e}")

# Example of an uncommon bug

def buggy_function(data):
    try:
        # This can raise KeyError if the key is not found
        value = data["missing_key"]
        return value
    except KeyError:
        # Incorrect error handling: return None instead of raising a more informative error
        return None

#Uncommon error:  Incorrect error handling
data = {}
result = buggy_function(data)
print(f"Result: {result}") #This will print None; better practice to raise custom Exception 


#Another Uncommon error: incorrect return type
def return_type_error(x):
    if isinstance(x,int):
        return str(x)
    else:
        return x

print(return_type_error(5)) # returns "5" instead of 5
print(return_type_error(5.2)) # Returns 5.2 

#Exception chaining and context
try:
    f = open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    try:
        # Attempt a backup strategy
        f = open("backup.txt", "r")
    except FileNotFoundError as e2:
        print(f"Error opening backup file: {e2}")
        raise  # Re-raise original exception for higher-level handling
    finally:
        f.close()