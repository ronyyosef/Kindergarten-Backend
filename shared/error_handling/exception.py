class MyException(Exception):
    def __init__(self, message, internal_code):
        super().__init__(message)
        self.internal_code = internal_code
        self.message = message

