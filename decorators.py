from datetime import datetime
from functools import wraps

def input_error(func):
    @wraps(func)
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except KeyError:
            return "Contact not found."
        except (ValueError, IndexError) as e:
            return f"{str(e).capitalize()}"
    return inner
