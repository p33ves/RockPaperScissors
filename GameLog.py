"""
Name : GameLog.py
Description : Logger-Decorator class for Rock-Paper-Scissor

"""


class RPS_Log:
    """
    Log Object updates the master log and creates session logs for individual sessions

    """
    import functools
    import logging

    def __init__(self, function):
        self.function = function

    def __call__(self, *args):
        print(f"Arguments are {args}")
        return self.function(self, *args)
