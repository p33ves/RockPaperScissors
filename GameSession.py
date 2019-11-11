"""
Name : GameSession.py
Description : Base round class for Rock-Paper-Scissor

"""

import uuid
import random
import msvcrt
from datetime import datetime
from GameRound import Round


validInput = set('p','r','s','q')

class Session:
    """
    Session object contains the unique session details and a list of round objects
    
    """

    def __init__(self, mood, uname = "Peeves"):
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
        

    def play(self):
        """
        Play function accepts the user input until user decides to quit

        """       
        while True: 
            print("Play your choice : ") 
            userInput = (msvcrt.getch()).lower()        
            if userInput in validInput:
                if userInput == 'q':
                    self.end_dt = str(datetime.utcnow())
                    if self.round_count > 0:
                        print(f"Thanks for playing, {self.uname} !")
                        self.session_record = self.rounds[-1].record
                    print("Exiting now")
                    return True
                else:
                    comp = random.choice(tuple('r','p','s'))
                    r = Round(userInput, comp)
                    self.round_count += 1
                    self.rounds += r.__repr__()
                    print(r)
            else:
                print("Play() game input Error !")
                return False
