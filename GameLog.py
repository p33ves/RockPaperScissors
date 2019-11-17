"""
Name : GameLog.py
Description : Logger-Decorator class for Rock-Paper-Scissor

"""

import functools
import logging

class RPS_Log:
    """
    Log Object updates the master log and creates session logs for individual sessions

    """

    def __init__(self, function):
        """
        GameLog constructor to set log configurations for different functions

        """
        self.function = function
        self.caller = str(function).split()[1].split('.')[0]
        if self.caller == "RPS_Session":
            logger = logging.getLogger(function)
            logger.setLevel(logging.INFO)
            formatter = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
            filehandler = logging.FileHandler('Session_logging.log')
            filehandler.setFormatter(formatter)
            logger.addHandler(filehandler)
            


        

    def __call__(self, *args):
        print(f"Function is {self.caller} of type {type(self.caller)} Arguments are {args}")
        return self.function(self, *args)
