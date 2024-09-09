
class InvalidUrl(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message
        self.status_code = 400

class InternalServerError(Exception):
    def __init__(self, message: str) -> None:
        super().__init__()
        self.message = message
        self.status_code = 500

