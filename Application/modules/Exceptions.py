class Error(Exception):
    """base class"""
    pass

class PasswardDidNotMatchError(Error):
    """Raised when passwards did not match"""
    def __init__(self,msg):
        self.message = msg
        print(msg)

class LengthNotEnoughError(Error):
    """Raised when length of the passwasd is less than limit"""
    def __init__(self,msg):
        self.message = msg
        print(msg)

class DoesNotContainCapitalLetterError(Error):
    """Raised when passward does not contain atleast one Capital letter"""
    def __init__(self,msg):
        self.message = msg
        print(msg)

class DoesNotContainDigitError(Error):
    """Raised when passward does not contain atleast one digit"""
    def __init__(self,msg):
        self.message = msg
        print(msg)

        
