class MyException(BaseException):
    def __init__(self, msg):
        self.__msg = msg
    
    def __str__(self):
        return self.__msg

raise MyException('My exception msg')