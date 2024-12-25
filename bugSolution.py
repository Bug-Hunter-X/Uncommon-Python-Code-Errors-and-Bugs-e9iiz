def function_with_uncommon_error(x):
    if x < 0:
        raise ValueError("x must be non-negative")
    elif x == 0:
        raise ZeroDivisionError("Cannot divide by zero")
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

#Improved handling of the KeyError exception
def improved_buggy_function(data):
    try:
        value = data["missing_key"]
        return value
    except KeyError:
        raise KeyError("The key 'missing_key' was not found in the data.")

#Corrected return type
def corrected_return_type_error(x):
    if isinstance(x,int):
        return x
    else:
        return x

print(corrected_return_type_error(5)) # returns 5
print(corrected_return_type_error(5.2)) # Returns 5.2

#Handling file errors
try:
    f = open("non_existent_file.txt", "r")
except FileNotFoundError as e:
    print(f"Error opening file: {e}")
    try:
        f = open("backup.txt", "w")
        f.write("Backup file created")
        f.close()
        print("Backup file created.")
    except FileNotFoundError as e2:
        print(f"Error creating backup file: {e2}")  # Handle the backup creation error as well.
    except Exception as e3:
        print(f"An unexpected error occurred: {e3}")
