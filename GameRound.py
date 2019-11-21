"""
Name : GameRound.py
Description : Base round class for Rock-Paper-Scissor

"""

import logging

round_logger = logging.getLogger("RoundLog")
round_logger.setLevel(logging.INFO)
round_formatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')  
with open(".session_id.temp") as temp_file:
    round_logfile = f"Session_{temp_file.readline()}.log"
round_filehandler = logging.FileHandler(round_logfile)                   
round_filehandler.setFormatter(round_formatter)
round_logger.addHandler(round_filehandler) 

def round_log_decorator(function):
    """
    """
    def log_wrapper(obj, *args):
        function(obj, *args)
        log_msg = obj.__repr__()
        round_logger.info(str(log_msg))
    return log_wrapper
 

class RPS_Round:
    """
    Round Object that includes information about what was played and the streak

    """
    record = {'win':0, 'loss':0, 'tie':0}

    @round_log_decorator
    def __init__ (self, session_id, user, comp):
        """
        Round object Constructor accepts input and updates the current record

        """
        self.session_id = session_id
        self.user = user
        self.comp = comp
        self.result = self.eval(user, comp)
        self.record[self.result] += 1
                                                                             
    def __repr__ (self):
        """
        Object representation of the round

        """
        return {'user':self.user , 'comp':self.comp , 'result':self.result , 'record':self.record}

    def __str__ (self):
        """
        Print the Round object in readable form for the user

        """
        return  f'''
        You played {self.display_fullform(self.user)} and computer played {self.display_fullform(self.comp)}. Result being a {self.result.capitalize()}.
        Current record is {self.record['win']} wins - {self.record['loss']} losses - {self.record['tie']} ties '''

    def eval (self,user, comp):
        """
        Evaluates and returns the round result

        """
        if user == comp :
            return 'tie'
        elif (user == 'r' and comp == 's') or (user == 'p' and comp == 'r') or (user == 's' and comp == 'p') :
            return 'win'
        else :
            return 'loss'

    def display_fullform(self,entry):
        """
        Returns the full form of the inputs

        """
        if entry == 'r' :
            return "Rock"
        elif entry == 'p' :
            return "Paper"
        elif entry == 's' :
            return "Scissors"
        else :
            return "Option Unrecognized"

