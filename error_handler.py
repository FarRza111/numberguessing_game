import random


class LessThanZero(Exception):
    def __init__(self, arg):
        self.msg = arg

class DigitError(Exception):
    def __init__(self, arg):
        self.msg = arg


class StringError(Exception):
    def __init__(self, arg):
        self.msg = arg
