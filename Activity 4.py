# ----Task 1

# call_count = 0

# def execute_task():
#     global call_count   
#     call_count += 1
#     print(f"Task executed {call_count} times")

# ----Task 2

# def math_operation(operator, *numbers):
#     if operator == "add":
#         return sum(numbers)
    
#     elif operator == "mul":
#         result = 1
#         for num in numbers:
#             result *= num
#         return result
    
#     else:
#         return "Invalid operator"

# ----Task 3

# def print_config(model_name, **hyperparams):
#     print(model_name.upper())
    
#     for key, value in hyperparams.items():
#         print(f"{key} ---->> {value}")

# ----Task 4

# def base_calculator(a, b, operation="sum"):
#     if operation == "sum":
#         return a + b
#     elif operation == "mul":
#         return a * b
#     else:
#         return "Invalid operation"


# def smart_wrapper(*args, **kwargs):
#     print("Logging: Function call initiated.")
    
#     return base_calculator(*args, **kwargs)

# ----Task 5

# def list_all_files(data):
    
#     if isinstance(data, dict):
#         for key, value in data.items():
#             print(f"Directory: {key}")
#             list_all_files(value)
    
#     elif isinstance(data, list):
#         for item in data:
#             list_all_files(item)
    
#     elif isinstance(data, str):
#         print(f"-> File: {data}")
    
#     else:
#         pass