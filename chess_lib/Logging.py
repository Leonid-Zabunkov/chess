from functools import wraps
from typing import Callable

logs: list[str] = []

def log_get(func: Callable):
    @wraps(func)
    def wrapper(self):
        logs.append(f"GET: {func.__qualname__}")
        return func(self)
    return wrapper

def log_set(func: Callable):
    @wraps(func)
    def wrapper(self, value):
        logs.append(f"SET: {func.__qualname__} = {value!r}")
        return func(self, value)
    return wrapper

def log_call(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # Методы класса имеют составное имя
        is_method = "." in func.__qualname__ and args
        
        # Нужно исключить self
        log_args = args[1:] if is_method else args
        args_str = [repr(a) for a in log_args]

        kwargs_str = [f"{k}={v!r}" for k, v in kwargs.items()]
        all_args = ", ".join(args_str + kwargs_str)
        
        logs.append(f"{func.__qualname__}({all_args})")
        
        return func(*args, **kwargs)
    return wrapper

def print_logs():
    print(*logs, sep="\n")