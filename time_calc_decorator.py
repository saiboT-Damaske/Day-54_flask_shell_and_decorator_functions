import time

current_time = time.time()
print(current_time)


def speed_calc_decorator(function):
    def wrapper_fuction():
        time_1 = time.time()
        function()
        time_2 = time.time()
        dif = time_2 - time_1
        print(f"{function.__name__} run speed: {dif}s")

    return wrapper_fuction


@speed_calc_decorator
def fast_function():
    for i in range(10000000):
        i * i


@speed_calc_decorator
def slow_function():
    for i in range(100000000):
        i * i


fast_function()
slow_function()
