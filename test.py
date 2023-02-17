from functools import wraps

def decore(func):
    @wraps(func)
    def wrapper(*agrs, **kwargs):
        # first
        result = func(*agrs, **kwargs)
        # result + fin
        return result
    return wrapper