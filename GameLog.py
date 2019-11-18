"""
Name : GameLog.py
Description : self.logger-Decorator class for Rock-Paper-Scissor

"""

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


        

    def __call__(self, *args):
        print(f"Function is {self.caller} of type {type(self.caller)} Arguments are {args}")
        self.logger = logging.getLogger(self.caller)
        self.logger.setLevel(logging.INFO)
        formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
        log_file = f"Session_{args[0]}.log"
        filehandler = logging.FileHandler(log_file)                   
        filehandler.setFormatter(formatter)
        self.logger.addHandler(filehandler)
        self.logger.info(str(args))
        return self.function(self, *args)
