"""
Name : GameSession.py
Description : Base round class for Rock-Paper-Scissor

"""

import uuid
import random
import msvcrt
from datetime import datetime
from GameRound import RPS_Round


validInput = set(['p','r','s','q'])

class RPS_Session:
    """
    Session object contains the unique session details and a list of round objects
    
    """

    def __init__(self, uname = "Peeves"):
        """
        Session object Constructor creates a unique session id, gets player mood and start time.
        It logs the details in SessionMaster.log

        """
        self.sid = str(uuid.uuid4())
        self.uname = uname
        print(f"Welcome {uname} !")
        self.mood = input("How are you feeling today?")  #Get input for user mood from 1 (depressed) to 5 (elated)
        self.start_dt = str(datetime.utcnow())
        self.round_count = 0
        self.rounds = []
        self.play()

    def __repr__ (self):
        """
        Object representation of the session

        """
        return {'session_id':self.sid, 'user':self.uname, 'mood':self.mood, 'start':self.start_dt, 'end':self.end_dt, 'round_count':self.round_count, 'record':self.session_record}
       
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
        while True: 
            print 
            userInput = (input("Play your choice : ")).lower()
            if userInput in validInput:
                if userInput == 'q':
                    self.end_dt = str(datetime.utcnow())
                    if self.round_count > 0:
                        print(f"Thanks for playing, {self.uname} !")
                        self.session_record = self.rounds[-1]['record']
                    print("Quiting now")
                    return True
                else:
                    comp = random.choice(tuple(['r','p','s']))
                    r = RPS_Round(userInput, comp)
                    self.round_count += 1
                    self.rounds.append(r.__repr__()) 
                    print(r)
            else:
                print("Play() game input Error !")
                return False


s = RPS_Session()
print(s)