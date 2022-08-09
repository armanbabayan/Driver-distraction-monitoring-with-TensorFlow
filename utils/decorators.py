import time


def timer(function):
    """
     This function shows the execution time of  the function decorated function.

    :param function: the function to be decorated
    :return: returns  the execution time of the function in seconds


    start_time contains the starting time of the function
    end_time contains the end  time of the function
    run_time is the difference between end_time and start_time which will be the execution time
    Then we print the execution time with 4 precision
    After that we return the result of the decorated function
    """
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        result = function(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = (end_time - start_time) / 60
        print(f"Finished {function.__name__!r} in {run_time: .2f} minutes")
        return result
    return wrapper_timer

