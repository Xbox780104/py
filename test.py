# input_values = list(map(float, input().split(",")))
# print(input_values)
# a=[1,2,34,5.0]
# print(type(a[0]),type(a[3]))

import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        return result, end_time - start_time
    return wrapper

@timer
def n_minmax(*args):
    if len(args) == 0:
        return None
    # Convert args to floating-point numbers with one decimal place
    args = [round(float(arg), 1) for arg in args]
    min_val = min(args)
    max_val = max(args)
    return (min_val, max_val)

# Example usage
if __name__ == "__main__":
    input_values = list(map(float, input().split(",")) )
    input_values = [round(value, 1) for value in input_values]
    result, execution_time = n_minmax(*input_values)
    print("程序计时完成！")
    print(result)