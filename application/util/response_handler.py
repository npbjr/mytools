from typing import Any, Callable, Type
import json
from decorators import handle_response


class ACCESS_DENIED:
    STATUS: int = 401
    MESSAGE: str = "Access Denied"


class BAD_REQUEST:
    STATUS: int = 400
    MESSAGE: str = "Bad Request"


class INTERNAL_SERVER_ERRPR:
    STATUS: int = 500
    MESSAGE: str = "Internal Server Error"


class INVALID_URL: ...


class DB_ERROR: ...


STATUS_MAPPING = {401: ACCESS_DENIED, 400: BAD_REQUEST, 500: INTERNAL_SERVER_ERRPR}


class Raise:
    def __init__(self, status_code: int) -> dict:
        exception_obj = STATUS_MAPPING.get(status_code)
        if exception_obj:
            self.STATUS = exception_obj.STATUS
            self.MESSAGE = exception_obj.MESSAGE
        else:
            exception_obj = STATUS_MAPPING.get(500)  # fallback
            self.STATUS = exception_obj.STATUS
            self.MESSAGE = exception_obj.MESSAGE

    @handle_response(cfunc=lambda x: json.loads(x))
    def __str__(self) -> dict:
        return json.dumps({"message": self.MESSAGE, "status": self.STATUS})

    def __call__(self) -> dict:
        return {"message": self.MESSAGE, "status": self.STATUS}
