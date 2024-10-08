from typing import Any, Callable, Type
import json
from functools import wraps

class CustomJsonEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, str):
            return json.dumps(str)
        return super().default(obj)

def firehose(payload: object): ...
def log_incomming_request(f: Callable[..., Any]): ...
def log_incomming_response(f: Callable[..., Any]): ...
def handle_request(func): ...
def handle_response(cfunc: Callable[..., Any]):
    """
    to be used for future logging implementation
    
    """
    def wrapper_function(func, *args, **kwargs):
        @wraps(func)
        def inner(*args, **kwargs):
            func_result = cfunc
            (
                func(*args, **kwargs)
                ) if cfunc else ...
            (
                log_incomming_response(firehose(func_result))
                if func_result.get("status", None)
                else ...
            )
            #convert it back to str
            return json.dumps(func_result)
        return inner
    return wrapper_function
