class InsufficientFundException(BaseException):
    def __init__(self, message):
        super().__init__(message)


class InvalidAccountException(BaseException):
    def __init__(self, message):
        super().__init__(message)



class InvalidAmountException(BaseException):
    def __init__(self, message):
        super().__init__(message)


class InvalidPinException(BaseException):
    def __init__(self, message):
        super("Message").__init__(message)
