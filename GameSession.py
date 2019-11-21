"""
Name : GameSession.py
Description : Session class for Rock-Paper-Scissor

"""


import uuid
import random
import GameRound
import logging
from datetime import datetime


validInput = set(['p','r','s','q'])

def log_decorator(function):
    """
    """
    caller = str(function).split()[1].split('.')[0]
    if caller == "RPS_Session":
        logger = sessionLogger
    def log_wrapper(obj, *args):
        function(obj, *args)
        log_msg = obj.__repr__()
        logger.info(str(log_msg))
    return log_wrapper

sessionLogger = logging.getLogger("SessionLog")
sessionLogger.setLevel(logging.INFO)
sessionFormatter = logging.Formatter('%(levelname)s:%(asctime)s:%(message)s')
sessionLogFile = "SessionMaster.log"
sessionFilehandler = logging.FileHandler(sessionLogFile)                   
sessionFilehandler.setFormatter(sessionFormatter)
sessionLogger.addHandler(sessionFilehandler)


class RPS_Session:
    """
    Session object contains the unique session details and a list of round objects
    
    """
    @log_decorator
    def __init__(self, uname, mood):
        """
        Session object Constructor creates a unique session id, gets player mood and start time.
        It logs the details in SessionMaster.log

        """
        self.session_id = str(uuid.uuid4())
        self.uname = uname
        print(f"Welcome {uname} ! \n Feeling {mood} today?")
        self.mood = mood  
        self.start_dt = str(datetime.utcnow())
        self.end_dt = self.round_count = self.session_record = None 
                                                                                       
    def __repr__ (self):
        """
        Object representation of the session

        """
        #return vars(self)
        return {'session_id':self.session_id, 'user':self.uname, 'mood':self.mood, 'start':self.start_dt, 'end':self.end_dt, 'round_count':self.round_count, 'record':self.session_record}
       
    def __str__ (self):
        """
        Print the Session object in readable form for the user

        """
        output = f'''
            Here's your session summary, {self.uname}...
            You played {self.round_count} games from {self.start_dt} till {self.end_dt}. \n'''
        if self.round_count:
            output += " And your record was {self.session_record}. Hope to play you again! "
        return output
    
    def play(self):
        """
        Play function accepts the user input until user decides to quit

        """
        self.round_count = 0
        self.rounds = []       
        while True: 
            userInput = (input("Play your choice : ")).lower()
            if userInput in validInput:
                if userInput == 'q':
                    return True
                else:
                    comp = random.choice(tuple(['r','p','s']))
                    r = GameRound.RPS_Round(self.session_id, userInput, comp)
                    self.round_count += 1
                    self.rounds.append(r.__repr__()) 
                    print(r)
            else:
                print("Play() game input Error !")
                return False

    @log_decorator
    def quit(self):
        """
        """
        self.end_dt = str(datetime.utcnow())
        if self.round_count > 0:
            print(f"Thanks for playing, {self.uname} !")
            self.session_record = self.rounds[-1]['record']
        else:
            print("Quiting without playing")
        return True


uname = input("Please enter your user name:")
mood = input("How are you feeling today?")    #Get input for user mood from 1 (depressed) to 5 (elated)
s = RPS_Session(uname,mood)
if s.play():
    s.quit()