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
        self.logger = logging.getLogger(self.caller)
        self.logger.setLevel(logging.INFO) 


    def __call__(self, *args):
        """
        """
        print(f"Function is {self.caller} of type {self.function} Arguments are {args}  while KeyWord Arguments are {args}")
        if self.caller == "RPS_Session":
            self.log_file = "SessionMaster.log"
            self.formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
        elif self.caller == "RPS_Round":
            self.log_file = f"Session_{args[0]}.log"
            self.formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
        self.filehandler = logging.FileHandler(self.log_file)                   
        self.filehandler.setFormatter(self.formatter)
        self.logger.addHandler(self.filehandler)
        obj = self.function(*args)
        self.logger.info(str(obj.__repr()))
        #return self.function(self, *args)
