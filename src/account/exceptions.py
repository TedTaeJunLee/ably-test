class AlreadyExistUserError(BaseException):
    pass


class UserDoesNotExistError(BaseException):
    pass


class WrongPasswordError(BaseException):
    pass
