from typing import Any, Callable, Type


def firehose(payload: object): ...
def log_incomming_request(f: Callable[..., Any]): ...
def log_incomming_response(f: Callable[..., Any]): ...


def handle_request(func): ...


def handle_response(func):
    def wrapper_function(self, *args, **kwargs):
        func_result = func(self, *args, **kwargs)
        (
            log_incomming_response(firehose(func_result))
            if func_result.get("status")
            else ...
        )
        return func_result

    return wrapper_function
