from datetime import datetime

def run_time(func, *args, **kwargs):
    start = datetime.now()
    print(f"Start time: {start}")
    result = func(*args, **kwargs)
    end = datetime.now()
    print(f"End time: {end}")
    print(f"Run Time: {end-start}")
    return result

def run_time_for_test(func, *args, **kwargs):
    start = datetime.now()
    result = func(*args, **kwargs)
    end = datetime.now()
    return result, end-start